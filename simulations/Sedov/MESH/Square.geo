side = 2.0;
npts = 65;  // 33

Point(1) = {0, 0, 0, 1};
Point(2) = {side, 0, 0, 1};
Point(3) = {side, side, 0, 1};
Point(4) = {0, side, 0, 1};

Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 1};

Curve Loop(1) = {1, 2, 3, 4};
Plane Surface(1) = {1};

Transfinite Curve{1, 2, 3, 4} = npts;
Transfinite Surface{1};
Recombine Surface{1};

Extrude {0.0, 0.0, 1.0} {
  Surface{1}; Layers{1}; Recombine;
}

Physical Surface("left") = {25};
Physical Surface("bottom") = {13};
Physical Surface("right") = {17};
Physical Surface("top") = {21};
Physical Surface("back") = {1};
Physical Surface("front") = {26};
Physical Volume("domain") = {1};
