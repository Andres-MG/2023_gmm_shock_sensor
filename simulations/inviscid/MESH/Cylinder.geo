wall_size = 0.04;
far_size = 0.1;
wake_size = 0.06;

in_offset = 1.2;
out_offset = 6.8;
channel_width = 2.0;

wall_width = 0.1;
wake_length = 6.3;
wake_width = 0.5;


Point(1) = {0, 0, 0, wall_size};
Point(2) = {-0.5, 0, 0, wall_size};
Point(3) = {0, 0.5, 0, wall_size};
Point(4) = {0.5, 0, 0, wall_size};
Point(5) = {0, -0.5, 0, wall_size};

Circle(1) = {3, 1, 4};
Circle(2) = {4, 1, 5};
Circle(3) = {5, 1, 2};
Circle(4) = {2, 1, 3};

Point(6)  = {-in_offset, -channel_width, 0, far_size};
Point(7)  = {out_offset, -channel_width, 0, far_size};
Point(8)  = {out_offset, channel_width, 0, far_size};
Point(9)  = {-in_offset, channel_width, 0, far_size};
Point(10) = {0.5 + wake_length, 0, 0, wake_size};

Line(5) = {6, 7};
Line(6) = {7, 8};
Line(7) = {8, 9};
Line(8) = {9, 6};
Line(9) = {4, 10};

Curve Loop(1) = {5, 6, 7, 8};
Curve Loop(2) = {1, 2, 3, 4};
Plane Surface(1) = {1, 2};

Recombine Surface {1};

Field[1] = Distance;
Field[1].CurvesList = {9};
Field[1].Sampling = 1000;

Field[2] = Threshold;
Field[2].InField = 1;
Field[2].DistMax = channel_width;
Field[2].DistMin = wake_width;
Field[2].SizeMax = far_size;
Field[2].SizeMin = wake_size;

Field[3] = Distance;
Field[3].CurvesList = {1, 2, 3, 4};
Field[3].Sampling = 1000;

Field[4] = Threshold;
Field[4].InField = 3;
Field[4].DistMax = channel_width;
Field[4].DistMin = wall_width;
Field[4].SizeMax = far_size;
Field[4].SizeMin = wall_size;

Field[5] = Min;
Field[5].FieldsList = {2, 4};

Background Field = 5;

out() = Extrude {0, 0, 1} {
  Surface{1}; Layers {1}; Recombine;
};

Periodic Surface{out(0)} = {1} Translate {0, 0, 1};

Mesh.ElementOrder = 2;
Mesh.HighOrderOptimize = 2;

Physical Surface("Back") = {1};
Physical Surface("Front") = {out(0)};
Physical Surface("Bottom") = {out(2)};
Physical Surface("Right") = {out(3)};
Physical Surface("Top") = {out(4)};
Physical Surface("Left") = {out(5)};
Physical Surface("Cylinder") = {out(6), out(7), out(8), out(9)};
Physical Volume("Domain") = {out(1)};
