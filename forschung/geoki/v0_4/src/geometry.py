"""Versioned Euler/geometry kernel: standard library, deterministic calculations."""
import math
def rotate(v,angle):
 x,y=v;c=math.cos(angle);s=math.sin(angle)
 return (c*x-s*y,s*x+c*y)
def rotate_complex(v,angle):
 z=complex(*v)*complex(math.cos(angle),math.sin(angle))
 return (z.real,z.imag)
def polygon_area(vertices):
 return abs(sum(x*vertices[(i+1)%len(vertices)][1]-y*vertices[(i+1)%len(vertices)][0] for i,(x,y) in enumerate(vertices)))/2
def polygon_area_triangulated(vertices):
 x0,y0=vertices[0]; return abs(sum(((vertices[i][0]-x0)*(vertices[i+1][1]-y0)-(vertices[i][1]-y0)*(vertices[i+1][0]-x0))/2 for i in range(1,len(vertices)-1)))
def euler_characteristic(v,e,f):return v-e+f
def euler_step(x,h,a):return x+h*a*x
def exponential_solution(x,h,a):return x*math.exp(a*h)

def translate(v,delta):return (v[0]+delta[0],v[1]+delta[1])
def reflect_x(v):return (v[0],-v[1])
def scale(v,s):return (s*v[0],s*v[1])
def affine(v,m,t):return (m[0][0]*v[0]+m[0][1]*v[1]+t[0],m[1][0]*v[0]+m[1][1]*v[1]+t[1])
def bezier2(p0,p1,p2,t):return tuple((1-t)**2*p0[i]+2*t*(1-t)*p1[i]+t*t*p2[i] for i in range(2))
def segment_intersection(a,b,c,d):
 def cross(x,y):return x[0]*y[1]-x[1]*y[0]
 v=(b[0]-a[0],b[1]-a[1]);w=(d[0]-c[0],d[1]-c[1]);u=(c[0]-a[0],c[1]-a[1]);den=cross(v,w)
 if abs(den)<1e-14:return None
 t=cross(u,w)/den;s=cross(u,v)/den
 return (a[0]+t*v[0],a[1]+t*v[1]) if 0<=t<=1 and 0<=s<=1 else None
