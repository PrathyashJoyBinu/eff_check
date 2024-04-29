import pandas as pd

class MathConverter:
    
    def __init__(self):
        self.df =self.data_loader()
        
    def data_loader(self):
        try:
            df =pd.read_csv("output/data.csv")
            df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
            return df
        
        except Exception as e:
            print("Error reading",e)
    
    def math_operations(self,airflow,production,selected_date):
        try:
            spc_airflow =self.specific_air_flow(airflow,production)
            avg_val = self.avg_10_days()
            percentage = self.percentage_increase(avg_val)
            
            data = {"Date":selected_date, "airflow":airflow, "production":production,"Specific_air_flow":spc_airflow,"Moving_average":avg_val,"Percentage_increase":percentage.get("val")}
            # self.df = self.df.append(data, ignore_index=True)
            new_row_df = pd.DataFrame(data, index=[0])
            self.df = pd.concat([self.df, new_row_df], ignore_index=True)
            self.df .to_csv("D:/freelance/project2/src/output/data.csv")
            
            return percentage
            
      
        except Exception as e:
            print("Error Math que",e)
            
   
   
   
   
    def specific_air_flow(self,airflow,production):
        try:
            spc_airflow = float(airflow)/float(production)
            print("spc_airflow",spc_airflow)
            return spc_airflow
        
        except Exception as e:
            print("Error Math Operation",e)
     
            
    
    
    def avg_10_days(self):
        try:
      
            avg_val =self.df["Moving_average"][-11:-1] 
            print("10 Days avg",avg_val.mean())
            return avg_val.mean()
        
        except Exception as e:
            print("Error Math Operation",e)
            
    
    def percentage_increase(self,avg_val):
        try:
            print("Percentage increase")
            spc_airflow_min = self.df["Specific_air_flow"].min()
            op1 = (avg_val - spc_airflow_min)*100
            op2 = spc_airflow_min
            val = op1/op2
            
            if val >10:
                print("System Anomaly")
                return {"st": False, "val": val}
            else:
                print("System Normal")
                return {"st": True, "val": val}
            
        except Exception as e:
            print("Error Math Operation",e)
   
        
        
            
                    