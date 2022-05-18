#CODE FOR AUTOMATING e-LEA3D WITH SET PARAMETERS GIVEN BY DR.ANDERSON:

# Using selenium to automate e-LEA3D website
from selenium import webdriver



#Opening the e-LEA3D website:
driver = webdriver.Chrome()
driver.get('https://chemoinfo.ipmc.cnrs.fr/LEA3D/index.html')




#Setting the Docking Function:
input_protein_file = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/fieldset/blockquote/table/tbody/tr[1]/td/li/input')
input_protein_file.send_keys('/Users/seleenjaber/Desktop/Bioinformatics Project /Protein PDB Files/2p7g_receptor.pdb')


set_coordinates_of_the_binding_site_x = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/fieldset/blockquote/table/tbody/tr[3]/td/li/p[2]/input[1]')
set_coordinates_of_the_binding_site_x.send_keys('48.55')

set_coordinates_of_the_binding_site_y = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/fieldset/blockquote/table/tbody/tr[3]/td/li/p[2]/input[2]')
set_coordinates_of_the_binding_site_y.send_keys('-26.96')

set_coordinates_of_the_binding_site_z = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/fieldset/blockquote/table/tbody/tr[3]/td/li/p[2]/input[3]')
set_coordinates_of_the_binding_site_z.send_keys('-97.44')

binding_site_radius = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/fieldset/blockquote/table/tbody/tr[3]/td/li/p[3]/input')
binding_site_radius.clear()
binding_site_radius.send_keys('16.0')


weight_in_final_score = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/fieldset/blockquote/table/tbody/tr[5]/td/li/input[1]')
weight_in_final_score.clear()
weight_in_final_score.send_keys('1.0')


#Setting up the Molecular Properties of the Ligand
min_molecular_weight = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[8]/td/fieldset/blockquote/table/tbody/tr[2]/td[2]/input')
min_molecular_weight.clear()
min_molecular_weight.send_keys('350')


max_molecular_weight = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[8]/td/fieldset/blockquote/table/tbody/tr[2]/td[3]/input')
max_molecular_weight.clear()
max_molecular_weight.send_keys('550')


final_molecular_weight = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[8]/td/fieldset/blockquote/table/tbody/tr[2]/td[4]/input')
final_molecular_weight.clear()
final_molecular_weight.send_keys('1')


min_number_of_h_donors = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[8]/td/fieldset/blockquote/table/tbody/tr[5]/td[2]/input')
min_number_of_h_donors.clear()
min_number_of_h_donors.send_keys('1')


max_number_of_h_donors = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[8]/td/fieldset/blockquote/table/tbody/tr[5]/td[3]/input')
max_number_of_h_donors.clear()
max_number_of_h_donors.send_keys('5')


final_weight_number_of_h_donors = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[8]/td/fieldset/blockquote/table/tbody/tr[5]/td[4]/input')
final_weight_number_of_h_donors.clear()
final_weight_number_of_h_donors.send_keys('1')


min_number_of_h_acceptors = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[8]/td/fieldset/blockquote/table/tbody/tr[6]/td[2]/input')
min_number_of_h_acceptors.clear()
min_number_of_h_acceptors.send_keys('1')


max_number_of_h_acceptors = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[8]/td/fieldset/blockquote/table/tbody/tr[6]/td[3]/input')
max_number_of_h_acceptors.clear()
max_number_of_h_acceptors.send_keys('10')


final_weight_number_of_h_acceptors = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[8]/td/fieldset/blockquote/table/tbody/tr[6]/td[4]/input')
final_weight_number_of_h_acceptors.clear()
final_weight_number_of_h_acceptors.send_keys('1')


final_weight_number_of_rotable_bonds = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[8]/td/fieldset/blockquote/table/tbody/tr[11]/td[4]/input')
final_weight_number_of_rotable_bonds.clear()
final_weight_number_of_rotable_bonds.send_keys('1')


min_number_of_aromatic_rings = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[8]/td/fieldset/blockquote/table/tbody/tr[13]/td[2]/input')
min_number_of_aromatic_rings.clear()
min_number_of_aromatic_rings.send_keys('1')


max_number_of_aromatic_rings = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[8]/td/fieldset/blockquote/table/tbody/tr[13]/td[3]/input')
max_number_of_aromatic_rings.clear()
max_number_of_aromatic_rings.send_keys('5')


final_weight_number_of_aromatic_rings = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[8]/td/fieldset/blockquote/table/tbody/tr[13]/td[4]/input')
final_weight_number_of_aromatic_rings.clear()
final_weight_number_of_aromatic_rings.send_keys('1')

# #Submit Parameters
submit_parameters = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[6]/td/center/input')
submit_parameters.click()

#  Enter Email Address for Results:
email_address_input = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[6]/td/input')
email_address_input.send_keys('seleej@uw.edu')


# #Selecting De Novo Design:
select_de_novo = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[7]/td/table/tbody/tr[1]/td[1]/input')
select_de_novo.click()

# Genetic Algorithm Parameters
num_of_generation = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[7]/td/table/tbody/tr[2]/td[1]/fieldset[1]/input')
num_of_generation.clear()
num_of_generation.send_keys('50')

pop_size = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[7]/td/table/tbody/tr[2]/td[1]/fieldset[1]/p[1]/input')
pop_size.clear()
pop_size.send_keys('40')


start_with_FDA_drugs = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[7]/td/table/tbody/tr[2]/td[1]/fieldset[1]/p[2]/input')
start_with_FDA_drugs.click()

# #Submit De Novo Design:
submit_de_novo = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[8]/td/center/input')
submit_de_novo.click()
