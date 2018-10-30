import csv
import logging
import math

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Aircraft:

	def __init__(self, air_database, init_mass, init_pos, init_vel, max_thrust, init_vect, chord, planform_area):
		self.mass = init_mass
		self.pos = [float(x) for x in init_pos]
		self.vel = [float(x) for x in init_vel]
		self.accel = [0.0,0.0]
		
		self.air = air_database
		
		self.vect = init_vect
		self.anti_vect = [-1*x for x in self.vect]
		self.chord = chord
		self.area = planform_area
		self.max_thrust = max_thrust
		
		self.weight = Force(self.weight_prop, [0,-1])
		self.lift = Force(0, [0,0])
		self.drag = Force(0, [0,0])
		self.thrust = Force(self.calc_thrust(), self.vect)
		self.normal = Force(0, [0,1])
		
	def calc_thrust(self):
				
		curr_thrust = self.max_thrust
		return curr_thrust
		
	def vel_mag(self):
		#velocity magnitude calculations
		
	def calc_vel(self):
		#general velocity calculations
		
	def calc_pos(self):
		#position calculations
				
	def time_step(self):
		#change in time calculation (delta t)
		
	def set_thrust(self,thrust):
		m_dot_prop = self.air*vel_mag*A
		m_dot_exhaust = self.air*self.calc_vel()*A
		
	def weight_prop(self):
		#weight of aircraft
		
	def calc_aoa(self):
		#calculate angle of attack from velocity and weight
	

class Atmosphere:

	def __init__(self,file_name):
        
		with open(file_name) as f:
			reader=csv.reader(f)
			atmos_csv=list(reader)
			
		atmos_csv.pop(0)
		self.alts=[float(line[0]) for line in atmos_csv]
		self.rhos=[float(line[7]) for line in atmos_csv]
		self.kinViscs=[float(line[14]) for line in atmos_csv]
		
	def getKinVisc(self, altitude, unit='ft'):
		
		print('alt for KinVisc: {} {}'.format(altitude, unit))
		
		if unit.lower() == 'meters' or unit.lower() == 'm':
			altitude=altitude*3.28084
			
		try:
			ind=self.alts.index(altitude)
			return self.kinViscs[ind]
			
		except ValueError:
			for i,alt in enumerate(self.alts):
			
				if altitude>alt and altitude<self.alts[i+1]:
				
					kinVisc=self.kinViscs[i]+(altitude-alt)*((self.kinViscs[i+1]-self.kinViscs[i])/(self.alts[i+1]-alt))
					
					return kinVisc
					
	def getRho(self, altitude, unit='ft'):
		
		print('alt for rho: {} {}'.format(altitude, unit))
		
		if unit.lower() == 'meters' or unit.lower() == 'm':
			altitude=altitude*3.28084
			
		try:
			ind=self.alts.index(altitude)
			return self.rho[ind]
			
		except ValueError:
			for i,alt in enumerate(self.alts):
				
				if altitude>alt and altitude<self.alts[i+1]:
					
					rho=self.rhos[i]+(altitude-alt)*((self.rhos[i+1]-self.rhos[i])/(self.alts[i+1]-alt))
					
					return rho

atmospheric_data=Atmosphere("C:\\Users\\ryano\\Desktop\\Atmospheric_Table.csv")
#kin_visc_100 = atmospheric_data.getKinVisc(100, 'meters')
#rho_100 = atmospheric_data.getRho(100, 'meters')
#print(kin_visc_100)
#print(rho_100)