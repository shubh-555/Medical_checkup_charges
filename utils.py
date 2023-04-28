import json
import pickle
import numpy as np


class body_checkup_charges():

    def __init__(self,data):
        self.data=data


    def loading_files(self):
        with open('artifacts/patient_data.json','r') as file:
            self.patient_data=json.load(file)

        with open('artifacts/rf_model.pkl','rb') as file:
            self.final_rf=pickle.load(file)   



    def charges_prediction(self):
        self.loading_files()


        user_data = np.zeros(len(self.patient_data['columns']))
        Area = self.data['html_Area']                         
        Children =self.data['html_Children']             
        Age = self.data['html_Age']                                      
        Income = self.data['html_Income']                         
        # Gender = eval(input('Gender:'))                
        # ReAdmis = eval(input('ReAdmis:'))               
        VitD_levels = self.data['html_VitD_levels']          
        Doc_visits = self.data['html_Doc_visits']            
        Full_meals_eaten = self.data['html_Full_meals_eaten']      
        VitD_supp = self.data['html_VitD_supp']            
        # Soft_drink = eval(input('Soft_drink:'))           
        Initial_admin = self.data['html_Initial_admin']         
        HighBlood = self.data['html_HighBlood']             
        # Stroke = eval(input('Stroke:'))               
        Complication_risk = self.data['html_Complication_risk']     
        Overweight = self.data['html_Overweight']           
        # Arthritis = eval(input('Arthritis:'))             
        # Diabetes = eval(input('Diabetes:'))              
        # Hyperlipidemia = eval(input('Hyperlipidemia:'))        
        BackPain = self.data['html_BackPain']              
        Anxiety = self.data['html_Anxiety']               
        # Allergic_rhinitis = eval(input('Allergic_rhinitis:'))     
        # Reflux_esophagitis = eval(input('Reflux_esophagitis:'))   
        # Asthma = eval(input('Asthma:'))                
        Services = self.data['html_Services']              
        Initial_days = self.data['html_Initial_days']          
        Additional_charges =self.data['html_Additional_charges']  






        user_data[0] = self.patient_data['Area'][Area]
        user_data[1] = Children
        user_data[2] = Age
        user_data[3] = Income
        # user_data[4] = user_data['Gender'][Gender]
        # user_data[5] = user_data['ReAdmis'][ReAdmis]
        user_data[4] = VitD_levels
        user_data[5] = Doc_visits
        user_data[6] = Full_meals_eaten
        user_data[7] = VitD_supp
        # user_data[10] = user_data['Soft_drink'][Soft_drink]
        user_data[8] = self.patient_data['Initial_admin'][Initial_admin]
        user_data[9] = self.patient_data['HighBlood'][HighBlood]
        # user_data[13] = user_data['Stroke'][Stroke]
        user_data[10] = self.patient_data['Complication_risk'][Complication_risk]
        user_data[11] = Overweight
        # user_data[16] = user_data['Arthritis'][Arthritis]
        # user_data[17] = user_data['Diabetes'][Diabetes]
        # user_data[18] = user_data['Hyperlipidemia'][Hyperlipidemia]
        user_data[12] = self.patient_data['BackPain'][BackPain]
        user_data[13] = Anxiety
        # user_data[21] = user_data['Allergic_rhinitis'][Allergic_rhinitis]
        # user_data[22] = user_data['Reflux_esophagitis'][Reflux_esophagitis]
        # user_data[23] = user_data['Asthma'][Asthma]
        user_data[14] = self.patient_data['Services'][Services]
        user_data[15] = Initial_days
        user_data[16] = Additional_charges

        result = self.final_rf.predict([user_data])
        result[0]



        

        return result
     


            