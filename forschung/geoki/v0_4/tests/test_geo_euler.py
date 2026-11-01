import unittest,math,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from geometry import *
class GeometryEuler(unittest.TestCase):
 def test_rotation_two_independent_methods(self):
  for a in (0,math.pi/8,math.pi/2,math.pi,2*math.pi):
   for p in ((1.,0.),(2.,-3.)):
    self.assertLess(math.dist(rotate(p,a),rotate_complex(p,a)),1e-12)
 def test_rotation_composition(self):
  p=(2.,3.);a=.37;b=-.81
  self.assertLess(math.dist(rotate(rotate(p,a),b),rotate(p,a+b)),1e-12)
 def test_inverse(self):
  p=(2.,-1.);a=.723
  self.assertLess(math.dist(rotate(rotate(p,a),-a),p),1e-12)
 def test_norm_invariant(self):
  p=(7.,-3.);r=rotate(p,1.23)
  self.assertAlmostEqual(math.hypot(*p),math.hypot(*r),places=12)
 def test_area(self):
  p=[(0,0),(3,0),(3,2),(0,2)]
  self.assertAlmostEqual(polygon_area(p),polygon_area_triangulated(p))
  self.assertAlmostEqual(polygon_area(p),6)
 def test_euler_topology_counterexample(self):
  self.assertEqual(euler_characteristic(8,12,6),2) # Cube
  self.assertEqual(euler_characteristic(16,32,16),0) # torus mesh, combinatorial counts
 def test_euler_step_is_approximation(self):
  exact=exponential_solution(1.,.1,1.)
  approx=euler_step(1.,.1,1.)
  self.assertGreater(abs(exact-approx),0)
  self.assertLess(abs(exact-approx),.006)
if __name__=="__main__":unittest.main()
