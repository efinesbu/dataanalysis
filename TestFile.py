##Test File
import numpy as np
# import matplotlib.pyplot as plt
#
# points = np.arange(-5,5,0.01)
# x, y = np.meshgrid(points,points)
# z = np.sqrt(x**2+y**2)
#
# plt.imshow(z, cmap=plt.cm.gray);plt.colorbar()
# plt.title("Plot of $\sqrt{x^2 + y^2}$ for a grid of values")
#
# plt.show()

import pandas as pd
from datetime import date
roster_location = 'C://Users/fine/Downloads/roster.csv' # Downloaded roster location
roster_table = pd.read_csv(roster_location, usecols=["Email", "SID"]) # Only read in critical columns
roster_table = roster_table.dropna(subset=['Email']) # Remove rows with missing emails
roster_table = roster_table.drop_duplicates(subset="SID") # Remove any potential duplicates
roster_SIDs = np.array(roster_table["SID"]) # Select SIDs

dl_location = 'C://Users/fine/Downloads/distributionlist.xlsx' # Download roster location
dl_table = pd.read_excel(dl_location, usecols="C") # Only read SIDs
dl_SIDs = np.array(dl_table["SID"]) # Select SIDs

new_mem = roster_SIDs[np.in1d(roster_SIDs, dl_SIDs, invert=True)] # Find new members: roster SIDs that are not in dl
removed_mem = dl_SIDs[np.in1d(dl_SIDs, roster_SIDs,invert=True)] # Find removed members: dl members that are not in roster
new_mem_count = len(new_mem) # New member count
removed_mem_count = len(removed_mem) # Removed member count

audit_location = 'C://Users/fine/PycharmProjects/dataanalysis/About Python/audit.csv' # CSV location of audit
audit_table = pd.read_csv(audit_location)

audit_log = pd.DataFrame({'Added': [new_mem_count], # Place audit data into DataFrame structure so it can be appended
                          'Removed': [removed_mem_count],
                          'Date': [date.today()]})

appended_audit = audit_table.append(audit_log, sort=False) # Add new audit to existing log
appended_audit.to_csv(audit_location, header=True, index=False) # Save audit file
