# ----------------------------------------------------------------------------------------------------
# IBM Confidential
# Licensed Materials - Property of IBM
# © Copyright IBM Corp. 2022  All Rights Reserved.
# US Government Users Restricted Rights -Use, duplication or disclosure restricted by 
# GSA ADPSchedule Contract with IBM Corp.
# ----------------------------------------------------------------------------------------------------

import pandas as pd

from ibm_common_scoring_utils.common.configuration import Configuration
from ibm_common_scoring_utils.utils.constants import ServiceProviderType, ModelType
from ibm_common_scoring_utils.clients.wml_provider import WMLProvider
from ibm_common_scoring_utils.clients.custom_ml_provider import CustomMLProvider
from ibm_common_scoring_utils.clients.aws_provider import AmazonSageMakerProvier
from ibm_common_scoring_utils.clients.azure_studio_provider import AzureStudioProvider
from ibm_common_scoring_utils.clients.azure_service_provider import AzureServiceProvider
from ibm_common_scoring_utils.clients.spss_provider import SPSSProvider
from ibm_common_scoring_utils.utils.scoring_utils_logger import ScoringUtilsLogger
from ibm_common_scoring_utils.utils.data_time_util import DateTimeUtil


logger = ScoringUtilsLogger(__name__)

class ScoreFactory():
    def __init__(self,config: Configuration):
        self.config  = config
        self.service_type = self.config.service_type

    def score(self, df:pd.DataFrame, include_features_in_response:bool=False):
        """
            Factory method to score the model 
        """
        logger.log_info(f"Scoring started with scoring_url {self.config.scoring_url}")
        start_time = DateTimeUtil.current_milli_time()
        if self.service_type == ServiceProviderType.WML.value:
            score_response =  WMLProvider(self.config).score(df)
        elif self.service_type == ServiceProviderType.CUSTOM_ML.value:
            score_response =  CustomMLProvider(self.config).score(df)
        elif self.service_type == ServiceProviderType.AWS.value:
            score_response =  AmazonSageMakerProvier(self.config).score(df)
        elif self.service_type == ServiceProviderType.AZURE_STUDIO.value:
            score_response =  AzureStudioProvider(self.config).score(df)
        elif self.service_type == ServiceProviderType.AZURE_SERVICE.value:
            score_response =  AzureServiceProvider(self.config).score(df)
        elif self.service_type == ServiceProviderType.SPSS.value:
            score_response =  SPSSProvider(self.config).score(df)
        else:
            raise NotImplementedError(f"Scoring support for {self.service_type} is not implemented")


        #Consider output columns
        output_cols = [self.config.prediction,self.config.probability]
        if self.config.model_type == ModelType.REGRESSION.value:
                output_cols.remove(self.config.probability)
        
        #Join input and output dfs 
        if include_features_in_response:
            feature_columns_to_consider = self.config.features + self.config.meta_fields
            score_response = pd.concat([df[feature_columns_to_consider],score_response[output_cols]],axis=1,join="inner")

        logger.log_info(f"Completed scoring with scoring_url {self.config.scoring_url}  in {DateTimeUtil.current_milli_time()-start_time}ms ")
        return score_response
