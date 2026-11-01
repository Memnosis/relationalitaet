import unittest,math,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from geometry import *
class Extra(unittest.TestCase):
 def test_translation_inverse(self):self.assertEqual(translate(translate((3,4),(5,-2)),(-5,2)),(3,4))
 def test_reflection_involution(self):self.assertEqual(reflect_x(reflect_x((2,7))),(2,7))
 def test_affine_rotation(self):
  a=.37;p=(2.,4.);m=((math.cos(a),-math.sin(a)),(math.sin(a),math.cos(a)))
  self.assertLess(math.dist(affine(p,m,(0,0)),rotate(p,a)),1e-12)
 def test_bezier_ends(self):
  self.assertEqual(bezier2((0,0),(2,3),(4,0),0),(0,0));self.assertEqual(bezier2((0,0),(2,3),(4,0),1),(4,0))
 def test_crossing(self):self.assertEqual(segment_intersection((0,0),(2,2),(0,2),(2,0)),(1,1))
 def test_parallel(self):self.assertIsNone(segment_intersection((0,0),(1,0),(0,1),(1,1)))
 def test_scale_norm(self):self.assertAlmostEqual(math.hypot(*scale((3,4),2)),10)
