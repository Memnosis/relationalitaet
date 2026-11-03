import math,sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from geometry import *
class GeoCompositionExtension(unittest.TestCase):
 def test_rotation_translation_inverse(self):
  p=(3.,4.);a=.67;d=(7.,-5.)
  q=translate(rotate(p,a),d)
  back=rotate(translate(q,(-d[0],-d[1])),-a)
  self.assertLess(math.dist(p,back),1e-12)
 def test_affine_vs_sequential(self):
  p=(2.,-4.);a=.92;d=(-3.,7.)
  m=((math.cos(a),-math.sin(a)),(math.sin(a),math.cos(a)))
  self.assertLess(math.dist(affine(p,m,d),translate(rotate(p,a),d)),1e-12)
 def test_area_under_rotation(self):
  polygon=[(1,0),(5,0),(5,3),(1,3)]
  self.assertAlmostEqual(polygon_area(polygon),polygon_area([rotate(x,.47) for x in polygon]),places=10)
 def test_scale_is_not_norm_invariant(self):
  p=(3.,4.);self.assertNotAlmostEqual(math.hypot(*p),math.hypot(*scale(p,2)))
 def test_collinear_area_zero(self):
  self.assertEqual(polygon_area([(0,0),(1,1),(2,2)]),0)
