# Reference: https://blog.naver.com/PostView.naver?blogId=seodaewoo&logNo=222043145688&parentCategoryNo=&categoryNo=62&viewDate=&isShowPopularPosts=false&from=postView

import tensorflow as tf
import numpy as np
import pandas as pd

from genet.predict.PredUtils import *
from genet.models import LoadModel


class CasVariant:
    def __init__(self, effector:str):
        '''DeepSpCas9variants score function

        The list_target30 should have a 30bp sequence in the form of a list.
        
        example) 
        >>> list_target30 = [
                        'TCACCTTCGTTTTTTTCCTTCTGCAGGAGG',
                        'CCTTCGTTTTTTTCCTTCTGCAGGAGGACA',
                        'CTTTCAAGAACTCTTCCACCTCCATGGTGT',
                        ]
        \n
        '''

        self.effector = effector

        self.model_info = LoadModel('DeepSpCas9variants', effector)
        self.model_dir  = self.model_info.model_dir


    def predict(self, list_target30: list) -> pd.DataFrame:
        '''Input으로 30nt target context sequence 들이 담긴 list가 들어오면,
        각 sequence 마다의 prediction score를 계산해서 list로 return 하는 함수
        '''
        dataset_ = pd.DataFrame()
        dataset_['target + PAM'] = list_target30

        # TFLite model loading / allocate tensor
        interpreter =  tf.lite.Interpreter('%s/DeepCas9variants_model_WeightQuantization.tflite' % self.model_dir)
        interpreter.allocate_tensors()

        # 입출력 텐서 가져오기
        input_details  = interpreter.get_input_details()
        output_details = interpreter.get_output_details()

        # 입력값 만들기 (preprocessing)
        dataset_seq_masked = preprocess_seq(list_target30, 30)
        dataset_seq_masked = pd.Series(list(dataset_seq_masked), name='seq')
        dataset_all = pd.concat([dataset_,dataset_seq_masked], axis=1)

        X_test_seq = np.stack(dataset_all['seq']).astype(np.float32)
        list_out = []

        for input_seq in X_test_seq:
            input_seq = np.reshape(input_seq, (1, 30, 4))

            # Set the input tensor data
            interpreter.set_tensor(input_details[0]['index'], input_seq)

            # Run the inference
            interpreter.invoke()

            # Get the predictions
            predictions = interpreter.get_tensor(output_details[0]['index'])
            list_out.append(predictions[0][0])

        df_out = pd.DataFrame()
        df_out['Target'] = list_target30
        df_out['Spacer'] = [seq[4:24] for seq in list_target30]

        df_out[self.effector] = list_out

        return df_out   



def cas_variant_score_original(list_target30:list, gpu_env=0):
    '''DeepSpCas9variants score function
    The list_target30 should have a 30bp sequence in the form of a list.
    
    If you want to use a different GPU (based on nvidia-smi),
    You can put the GPU number in the gpu_env. \n
    
    example) 
    >>> list_target30 = [
                        'TCACCTTCGTTTTTTTCCTTCTGCAGGAGG',
                        'CCTTCGTTTTTTTCCTTCTGCAGGAGGACA',
                        'CTTTCAAGAACTCTTCCACCTCCATGGTGT',
                        ]

    >>> list_out = cas_variant_score(list_target30)
    '''
    header=['target + PAM','feature']

    dataset_ = pd.read_csv('/media/2400_new/GS/DeepBE/PAM/PAM_variant_NG/PAM_variant_input_example.csv',header=None,names=header)
    # final_model =  tf.keras.models.load_model('/media/2400_new/GS/DeepBE/models/PAM/PAM_variant_NG_model.h5',compile=False)

    # TFLite model loading / allocate tensor
    interpreter =  tf.lite.Interpreter('/media/2400_new/GS/DeepBE/models/PAM/PAM_variant_NG_model_WeightQuantization.tflite')
    interpreter.allocate_tensors()

    # 입출력 텐서 가져오기
    input_details  = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # 입력값 만들기 (preprocessing)
    dataset_seq_masked = preprocess_seq(dataset_['target + PAM'],30)
    dataset_seq_masked = pd.Series(list(dataset_seq_masked),name='seq')
    dataset_all = pd.concat([dataset_,dataset_seq_masked],axis=1)

    X_test_seq = np.stack(dataset_all['seq']).astype(np.float32)

    # Set the input tensor data
    interpreter.set_tensor(input_details[0]['index'], X_test_seq)

    # Run the inference
    interpreter.invoke()

    # Get the predictions
    predictions = interpreter.get_tensor(output_details[0]['index'])

    # 'predictions' contains the predicted values for the input data using the TFLite model
    return predictions    