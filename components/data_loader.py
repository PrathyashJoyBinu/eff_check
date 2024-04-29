import pandas as pd

class DataOperator():
    def __init__(self):
        self.df = self.data_loader()
        

    def data_loader(self):
        try:
            df =pd.read_csv("output/data.csv")
            df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

          
            return df
        except Exception as e:
            print("Error reading",e)
            
    def display_chart(self):
        air_flow = self.df["airflow"]
        production = self.df["production"]
        date= self.df["Date"]
        specific_air_flow = self.df["Specific_air_flow"]
        percentage = self.df["Percentage_increase"]
      
        data ={"air_flow":air_flow, "production":production, "date":date,"specific air_flow":specific_air_flow,"percentage":percentage}
        
        return pd.DataFrame(data)
    
    def threshold_breaker(self):
        return (self.df["Percentage_increase"]>10).sum()
    
    def data_view(self):
        return self.df
            
    # def save_data(self,air_flow,date,production,Specific_air_flow,Moving_average):
    #     data = {"air_flow":air_flow, "production":production,
        
            
