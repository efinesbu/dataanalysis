'''

This script automates the identification of new and removed members to maintain an updated distribution list
and automatically updates an audit file.

1st file contains the updated roster, downloaded from a website
2nd file contains the current distribution list (dl), downloaded from dl management location
3rd file contains the audit log of updates, stored locally with the Communications and/or Membership Chair

Required downloads: numpy, pandas, xlsxwriter

'''
import numpy as np
import pandas as pd
from datetime import date

roster_location = 'C://Users/fine/Downloads/roster.csv' # Downloaded roster location
roster_table = pd.read_csv(roster_location, usecols=["Email", "SID"]) # Only read in SID & Email columns
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

audit_location = 'C://Users/fine/PycharmProjects/dataanalysis/About Python/audit.xlsx' # CSV location of audit
writer = pd.ExcelWriter(audit_location, engine='xlsxwriter')

audit_table = pd.read_excel(audit_location)
audit_log = pd.DataFrame({'Added': [new_mem_count], # Place audit data into DataFrame structure so it can be appended
                          'Removed': [removed_mem_count],
                          'Date': [date.today()]})
appended_audit = audit_table.append(audit_log, sort=False) # Add new audit to existing log
appended_audit.to_excel(writer, sheet_name='Audit', index=False) # Save audit file

add = pd.DataFrame({"Add":new_mem,})
add.to_excel(writer, sheet_name='Add', index=False) # Save audit file

remove = pd.DataFrame({"Remove":removed_mem,})
remove.to_excel(writer, sheet_name='Remove', index=False) # Save audit file

writer.save()
writer.close()


######################################

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