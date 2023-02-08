import pickle
import json
import config
import numpy as np

class Cancer_Prediction():
    def __init__(self,radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, 
                concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, 
                texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, 
                symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, 
                smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst):
        self.radius_mean = radius_mean
        self.texture_mean = texture_mean
        self.perimeter_mean = perimeter_mean
        self.area_mean = area_mean
        self.smoothness_mean = smoothness_mean
        self.compactness_mean = compactness_mean
        self.concavity_mean = concavity_mean
        self.concave_points_mean = concave_points_mean
        self.symmetry_mean = symmetry_mean
        self.fractal_dimension_mean = fractal_dimension_mean
        self.radius_se = radius_se
        self.texture_se = texture_se
        self.perimeter_se =  perimeter_se
        self.area_se = area_se
        self.smoothness_se = smoothness_se
        self.compactness_se = compactness_se
        self.concavity_se = concavity_se
        self.concave_points_se = concave_points_se
        self.symmetry_se = symmetry_se
        self.fractal_dimension_se = fractal_dimension_se
        self.radius_worst = radius_worst
        self.texture_worst = texture_worst
        self.perimeter_worst = perimeter_worst
        self.area_worst = area_worst
        self.smoothness_worst = smoothness_worst
        self.compactness_worst = compactness_worst
        self.concavity_worst = concavity_worst
        self.concave_points_worst = concave_points_worst
        self.symmetry_worst = symmetry_worst
        self.fractal_dimension_worst = fractal_dimension_worst
        


    def load_model(self):
        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.model = pickle.load(f)

        with open(config.SCALE_FILE_PATH,"rb") as f:
            self.scaled_data = pickle.load(f)

        with open(config.JSON_FILE_PATH,"r") as f:
            self.json_data = json.load(f)


    def prediction(self):
        self.load_model()

        test_array = np.zeros(len(self.json_data["columns"]))


        test_array[0] = self.radius_mean
        test_array[1] = self.texture_mean
        test_array[2] = self.perimeter_mean
        test_array[3] = self.area_mean
        test_array[4] = self.smoothness_mean
        test_array[5] = self.compactness_mean
        test_array[6] = self.concavity_mean
        test_array[7] = self.concave_points_mean
        test_array[8] = self.symmetry_mean
        test_array[9] = self.fractal_dimension_mean
        test_array[10] = self.radius_se
        test_array[11] = self.texture_se
        test_array[12] = self.perimeter_se
        test_array[13] = self.area_se
        test_array[14] = self.smoothness_se
        test_array[15] = self.compactness_se
        test_array[16] = self.concavity_se
        test_array[17] = self.concave_points_se
        test_array[18] = self.symmetry_se
        test_array[19] = self.fractal_dimension_se
        test_array[20] = self.radius_worst
        test_array[21] = self.texture_worst
        test_array[22] = self.perimeter_worst
        test_array[23] = self.area_worst
        test_array[24] = self.smoothness_worst
        test_array[25] = self.compactness_worst
        test_array[26] = self.concavity_worst
        test_array[27] = self.concave_points_worst
        test_array[28] = self.symmetry_worst
        test_array[29] = self.fractal_dimension_worst

        test_array1=self.scaled_data.transform([test_array])

        predict = self.model.predict(test_array1)
        return predict