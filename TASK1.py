import pandas as pd
import matplotlib.pyplot as plt

def plot_sfd_bmd():
    try:
        # Read data 
        df = pd.read_csv(r"C:\Users\balar\Downloads\SFS_Screening_SFDBMD.csv")
        
        
        print("Columns in CSV:", df.columns.tolist())
        
        #  two subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Plot SFD
        ax1.plot(df['Distance (m)'], df['SF (kN)'], 'r-', linewidth=2)
        ax1.fill_between(df['Distance (m)'], df['SF (kN)'], color='red', alpha=0.3)
        ax1.set_title('Shear Force Diagram (SFD)')
        ax1.set_xlabel('Distance (m)')
        ax1.set_ylabel('Shear Force (kN)')
        ax1.grid(True)
        
        # Plot  BMD 
        ax2.plot(df['Distance (m)'], df['BM (kN-m)'], 'b-', linewidth=2)
        ax2.fill_between(df['Distance (m)'], df['BM (kN-m)'], color='blue', alpha=0.3)
        ax2.set_title('Bending Moment Diagram (BMD)')
        ax2.set_xlabel('Distance (m)')
        ax2.set_ylabel('Bending Moment (kNm)')
        ax2.grid(True)
        
        # Save 
        fig.savefig('sfd_bmd_results.png')
        print("Plots saved as 'sfd_bmd_results.png'")
        
        plt.show()
        
    except Exception as e:
        print(f"Error: {str(e)}")
     
# Execute
plot_sfd_bmd()