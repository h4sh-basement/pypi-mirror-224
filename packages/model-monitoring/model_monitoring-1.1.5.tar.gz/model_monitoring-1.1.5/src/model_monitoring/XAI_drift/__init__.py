import pandas as pd
import numpy as np
import warnings

from model_monitoring.utils import check_features_sets


class XAIDrift:
    """XAI Drift Class."""

    def __init__(self, xai_curr, xai_stor, feat_to_check=None):
        """XAI Drift Class.

        Args:
            xai_curr (dict): current xai dictionary.
            xai_stor (dict): historical xai dictionary.
            feat_to_check (list, optional): list of features to be checked. Deafualts to None.
        """
        # Check if the scores are assigned to the same set of features
        check_features_sets(
            features_1=list(xai_curr["feat_importance"].keys()), features_2=list(xai_stor["feat_importance"].keys())
        )
        list_com_features = list(
            set(xai_curr["feat_importance"].keys()).intersection(set(xai_stor["feat_importance"].keys()))
        )
        if len(list_com_features) == 0:
            raise ValueError("No features in common between the two sets")

        if feat_to_check is None:
            feat_to_check = list_com_features

        self.feat_to_check = feat_to_check
        self.xai_curr = {
            "type": xai_curr["type"],
            "feat_importance": {x: xai_curr["feat_importance"][x] for x in list_com_features},
        }
        self.xai_stor = {
            "type": xai_stor["type"],
            "feat_importance": {x: xai_stor["feat_importance"][x] for x in list_com_features},
        }

        # Check if the type of feature importance of historical and current xai model is the same
        if self.xai_curr["type"] != self.xai_stor["type"]:
            if (self.xai_curr["type"] == "coef") or (self.xai_stor["type"] == "coef"):
                raise ValueError(
                    f"'{self.xai_curr['type']}' type of feature importance in current xai model is not compatible with '{xai_stor['type']}' typ in historical xai model"
                )
            else:
                warnings.warn(
                    "the type of feature importance in current and historical xai model are not the same but they are compatible"
                )

        # Initialize the report
        xai_drift_report = (
            pd.DataFrame.from_dict(self.xai_curr["feat_importance"], "index", columns=["Curr_score"])
            .reset_index()
            .rename(columns={"index": "Feature"})
        )
        xai_stor_report = (
            pd.DataFrame.from_dict(self.xai_stor["feat_importance"], "index", columns=["Stor_score"])
            .reset_index()
            .rename(columns={"index": "Feature"})
        )
        try:
            xai_drift_report.loc[:, "Stor_score"] = xai_stor_report.Stor_score
        except Exception:
            xai_drift_report = xai_drift_report.merge(xai_stor_report, how="outer", on="Feature")

        self.xai_drift_report = xai_drift_report

    def get_drift(self, relative_red=0.4, relative_yellow=0.2, absolute_tol=0.1):
        """Load on the report the feature importance drift and relative alert from current and historical XAI model.

        Args:
            relative_red (float, optional): threshold for relative critical warning. Defaults to 0.4.
            relative_yellow (float, optional): threshold for relative medium warning. Defaults to 0.2.
            absolute_tol (float, optional): absolute threshold for relative warnings. Defaults to 0.1.
        """
        self.relative_red = relative_red
        self.relative_yellow = relative_yellow
        self.absolute_tol = absolute_tol

        # Generation Drift
        for a in self.xai_drift_report.Feature.values:
            stor_score = self.xai_drift_report.loc[self.xai_drift_report.Feature == a, "Stor_score"].values[0]
            curr_score = self.xai_drift_report.loc[self.xai_drift_report.Feature == a, "Curr_score"].values[0]
            self.xai_drift_report.loc[self.xai_drift_report.Feature == a, "Drift(%)"] = (
                (curr_score - stor_score) / stor_score * 100
            )

        # Generation Alert
        for a in self.xai_drift_report.Feature.values:
            stor_score = self.xai_drift_report.loc[self.xai_drift_report.Feature == a, "Stor_score"].values[0]
            curr_score = self.xai_drift_report.loc[self.xai_drift_report.Feature == a, "Curr_score"].values[0]
            if abs(curr_score - stor_score) >= self.absolute_tol:
                drift_xai = self.xai_drift_report.loc[self.xai_drift_report.Feature == a, "Drift(%)"].values[0]
                if abs(drift_xai) > self.relative_red * 100:
                    self.xai_drift_report.loc[self.xai_drift_report.Feature == a, "Relative_warning"] = "Red Alert"
                else:
                    if (abs(drift_xai) < self.relative_red * 100) and (abs(drift_xai) > self.relative_yellow * 100):
                        self.xai_drift_report.loc[
                            self.xai_drift_report.Feature == a, "Relative_warning"
                        ] = "Yellow Alert"
                    else:
                        self.xai_drift_report.loc[self.xai_drift_report.Feature == a, "Relative_warning"] = np.nan
            else:
                self.xai_drift_report.loc[self.xai_drift_report.Feature == a, "Relative_warning"] = np.nan

    def get_report(self):
        """Return the xai drift report.

        Returns:
            pd.DataFrame: report of the class.
        """
        return self.xai_drift_report.sort_values("Stor_score", key=abs)

    def plot(self):
        """Plot the report on features importance drift."""
        self.xai_drift_report.sort_values("Stor_score", key=abs).plot(
            x="Feature", y=["Curr_score", "Stor_score"], kind="barh", title="Features Importance Drift"
        )
