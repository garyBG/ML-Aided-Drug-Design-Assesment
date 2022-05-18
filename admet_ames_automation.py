#CODE FOR AUTOMATING ADMETLAB:


# Using selenium to automate ADMETLAB website
from selenium import webdriver

#Opening the ADMETLAB website:
driver = webdriver.Chrome()
driver.get('http://admet.scbdd.com/')


#Select ADME/T Evaluation
select_ADMET_evaluation = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div[7]/div[2]/p[4]/a')
select_ADMET_evaluation.click()


#Select AMES
select_AMES = driver.find_element_by_xpath('//*[@id="AMES"]/a')
select_AMES.click()

#inputting All Ligands for AMES Evaluation
input_sdf_files = driver.find_element_by_xpath('///*[@id="AMES"]/a').clear()
input_sdf_files.send_keys('/Users/seleenjaber/Desktop/Bioinformatics Project /All Protein-Ligand Files/all_ligands.sdf')

#change input type
select_upload_files = driver.find_element_by_xpath('//*[@id="way"]')
select_upload_files.click()

#Submit sdf file
submit_sdf = driver.find_element_by_xpath('//*[@id="b"]')
submit_sdf.click()
