wedge = 1.0/6.0;
width = 3.25;
height = 1.0;
hpts1 = 7;
hpts2 = 112;
vpts  = 37;

Point(1) = {0, 0, 0, 1};
Point(2) = {wedge, 0, 0, 1};
Point(3) = {width, 0, 0, 1};
Point(4) = {width, height, 0, 1};
Point(5) = {wedge, height, 0, 1};
Point(6) = {0, height, 0, 1};

Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 5};
Line(5) = {5, 6};
Line(6) = {6, 1};
Line(7) = {2, 5};

Curve Loop(1) = {1, 7, 5, 6};
Curve Loop(2) = {2, 3, 4, -7};

Plane Surface(1) = {1};
Plane Surface(2) = {2};

Transfinite Curve{1, -5} = hpts1;
Transfinite Curve{2, -4} = hpts2;
Transfinite Curve{3, -6, 7} = vpts;
Transfinite Surface{1, 2};
Recombine Surface{1, 2};

Extrude {0.0, 0.0, 1.0} {
  Surface{1}; Surface{2}; Layers{1}; Recombine;
}

Physical Surface("in_left") = {28};
Physical Surface("in_top") = {24, 46};
Physical Surface("out_right") = {42};
Physical Surface("out_bottom") = {16};
Physical Surface("wedge") = {38};
Physical Surface("back") = {2, 1};
Physical Surface("front") = {51, 29};
Physical Volume("domain") = {1, 2};
