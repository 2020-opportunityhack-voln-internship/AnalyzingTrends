# -*- coding: utf-8 -*-
from maindata import AppFunction
import time

class SuggestedFunction:


    
    def load_suggested(self,start,end):
        suggestedlist = SuggestedFunction.suggestedlist[start:end]
        total = int(end) - int(start)
        completed = 0
        for item in suggestedlist:
            print(item)
            AppFunction.app(0, item, 5, 'suggested')
            time.sleep(15)
            completed = int(completed) + 1
            remaining = total - completed
            print(str(remaining) + ' remaining \n\n')
    
    def suggested_html(self):
        suggestedhtmllist = []
        for item in SuggestedFunction.suggestedlist:
            itempath = str(item).replace(' ','-')
            item = "<option value =\"" + str(itempath) + "\">" + str(item) + "</option>"
            suggestedhtmllist.append(item)
        return suggestedhtmllist
    
    suggestedlist=['Biology', 'DNA', 'Homeostasis', 'Metabolism', 'Biosphere', 'Nucleus', 'Electron', 'Isotope', 'Osmosis', 'Ionic Bond', 'Covalent bond', 'Molecule', 'Carbohydrate', 'Nucleic Acid', 'Protein', 'Polymer', 'Amino Acid', 'Catalyst', 'Hydrogen Bond', 'pH scale', 'Cell', 'Cell Membrane', 'Cytoplasm', 'Ribosome', 'Cytoskeleton', 'Endoplasmic Reticulum', 'Biochemistry', 'Thermodynamics', 'Amino Acid', 'Proteins', 'Carbohydrates', 'Glycoconjugates', 'Lipids', 'Nucleotides', 'Enzyme', 'Metabolism', 'Photosynthesis', 'Environmental Science', 'Biosphere', 'Species', 'Ecosystem', 'Biotic factor', 'Abiotic factor', 'Ecology', 'Carnivore', 'Herbivore', 'Omnivore', 'Photosynthesis', 'Chemosynthesis', 'Detritivore', 'Food chain', 'Phytoplankton', 'Zooplankton', 'Ecological pyramid', 'Biomass', 'Nutrient', 'Denitrification', 'Global warming', 'Physics', 'Kinematics', 'Dynamics Force', 'Newton’s Law of Motion', 'Friction', 'Elasticity', 'Linear Momentum', 'Angular Momentum', 'Rotational Motion', 'Fluid Statics', 'Fluid Dynamics', 'Thermodynamics', 'Oscillatory Motion', 'Waves', 'Electric Charge', 'Electric Field', 'Circuits', 'Magnetism', 'Electromagnetic Waves', 'Wave optics', 'Quantum Physics', 'Nuclear Physics', 'Radioactivity', 'Atoms', 'Particle Physics', 'Atomic Masses', 'Radioactive Isotopes', 'Angular Momentum', 'Gravity', 'TECHNOLOGY', 'Technology', 'Hydraulics', 'Pneumatics', 'Pulleys', 'Gears', 'Orthographic', 'Static force', 'Dynamic force', 'Tension', 'Torsion', 'Compression', 'Shear', 'Bending', 'Density', 'Flow chart', 'Pascal’s Principle', 'Hydraulic Car jack', 'Brakes', 'Spur gears', 'Rotation', 'rpm', 'Gear ratio', 'Torque', 'Pinion gear', 'Rack gear', 'Lever', 'ENGINEERING', 'Aerospace Engineer', 'Fixed wing aircraft', 'Rotorcraft', 'Fuselage', 'Empennage', 'Barometric altitude', 'Viscosity', 'Airfoil', 'Aerodynamic', 'Aircraft Cockpits', 'Air conditioning', 'Turbine', 'Nozzles', 'Compressor', 'Combustion Chamber', 'Jet Engine', 'Turbojets', 'Turbofans', 'Longitudinal balancing', 'Mechanical Engineer', 'Automobile', 'Airplane', 'Circuits', 'Compressors', 'Heat transfer', 'Energy systems', 'Statics', 'Motion', 'Dynamics', 'Thermodynamics', 'Fluid mechanics', 'Solid mechanics', 'Linear motion', 'Reciprocating motion', 'Rotary motion', 'Oscillating motion', 'Linkage', 'Lever', 'Inclined plane', 'Wheel', 'Axle', 'Pulley', 'Crane', 'Gears', 'Cylindrical cam', 'Friction', 'Balancing beams', 'Buoyancy', 'Drag force', 'Translational Motion', 'Rotational Motion', 'Gravitational Potential Energy', 'Elastic Potential Energy', 'Kinetic Energy', 'Electrical Engineer', 'Sinusoid', 'Discrete-time signals', 'Voltage', 'Current', 'Circuit', 'Power dissipation', 'Capacitors', 'Inductors', 'Amplifiers', 'Amplitude', 'Fourier Series', 'Spectrograms', 'Wireline channels', 'Wireless channels', 'Message Routing', 'Transmission', 'Ethernet', 'Entropy', 'ARTS', 'Art History', 'Fine art', 'Mimesis', 'Plato', 'Abstract', 'Aesthetic', 'Postmodern', 'Enlightenment', 'Connoisseurship', 'Painting', 'Design', 'Formalism', 'Modernism', 'Modernity', 'Karl Marx', 'Freud', 'Lacan', 'Iconography', 'Iconology', 'Painting', 'Semiotics', 'Poststructuralism', 'Figurative Language', 'Social semiotics', 'Psychoanalysis', 'Psychoanalysis', 'Feminism', 'Photography', 'Surrealism', 'Creativity', 'MATH', 'Trigonometry', 'Right triangle', 'Trigonometric functions', 'Acute Angle', 'Obtuse angle', 'Right angle', 'Straight angle', 'Oblique triangle', 'Acute triangle', 'Obtuse triangle', 'Hypotenuse', 'Pythagorean Theorem', 'Euclid’s Formula', 'Cartesian coordinates', 'x-coordinate', 'y-coordinate', 'x-axis', 'y-axis', 'Quadrants', 'Even function', 'Odd function', 'Sine', 'Cosine', 'Tangent', 'Cosecant', 'Secant', 'Cotangent', 'Radians', 'Degrees', 'Radius', 'Midpoint', 'Arc length', 'Circular motion', 'Linear Speed', 'Angular Speed', 'Law of sines', 'Law of cosines', 'Law of tangents', 'Algebra I', 'Absolute value', 'Axis of symmetry', 'Boxplot', 'Coefficient', 'Coordinate plane', 'Correlation', 'Decimal', 'Denominator', 'Dot plot', 'Equation', 'Exponential growth', 'Exponential decay', 'Quartiles', 'Fraction', 'Integer', 'Inverse function', 'Irrational number', 'Linear model', 'Median', 'Monomial', 'Polynomial', 'Numerator', 'Outlier', 'Parabola', 'Parallel', 'Perfect square', 'Scatterplot', 'Slope', 'Square root', 'Standard deviation', 'Quadratic Formula', 'Geometry', 'Points', 'Lines', 'Planes', 'Segments', 'Congruence', 'Midpoint', 'Polygons', 'Perimeter', 'Circumference', 'Area', 'Angles', 'Parallel lines', 'Parallelogram', 'Transversals', 'Slope', 'Graphs', 'Perpendicular lines', 'Isosceles Triangle', 'Equilateral Triangles', 'Midsegment Theorem', 'Perpendicular Bisectors', 'Angle Bisectors', 'Medians', 'Geometric Mean', 'Ratios', 'Proportions', 'Pythagorean Theorem', 'Quadratic Equation', 'Tangent', 'Sine', 'Cosine', 'Quadrilaterals', 'Rhombus', 'Rectangle', 'Square', 'Triangle', 'Trapezoid', 'Binomial', 'Trinomial', 'Matrices', 'Vectors', 'Symmetry', 'Circles', 'Perimeter', 'Solids', 'Prisms', 'Cylinders', 'Sphere', 'Volume', 'Pyramids', 'Cones', 'Surface Area', 'Algebra II', 'Order of operations', 'Algebraic expression', 'Distributive property', 'Equation', 'Absolute value', 'Linear equation', 'Linear function', 'Slope', 'slope-intercept form', 'Point-slope form', 'System of equations', 'Substitution method', 'Elimination method', 'Linear programming', 'Matrix', 'Determinant', 'Cramer’s Rule', 'Matrix Equation', 'Scientific notation', 'Polynomial', 'FOIL method', 'Synthetic division', 'Complex number', 'Quadratic formula', 'Polynomial function', 'Synthetic substitution', 'Fundamental theorem of Algebra', 'Composition of functions', 'Inverse function', 'Parabola', 'Conic section', 'Circle', 'Ellipse', 'Hyperbola', 'Rational expression', 'Asymptote', 'Point discontinuity', 'Direct variation', 'Inverse variation', 'Exponential growth', 'Exponential decay', 'Logarithm', 'Arithmetic sequence', 'Arithmetic series', 'Sigma notation', 'Geometric sequence', 'Geometric series', 'Permutation', 'Probability', 'Variation', 'Right Triangle', 'Radian', 'Circular function', 'Law of sines', 'Law of cosines', 'Circular function', 'Amplitude', 'Phase shift', 'Statistics', 'Probability', 'Venn diagrams', 'Subsets', 'Conditional probability', 'Continuity', 'Proofs', 'Random variables', 'Discrete variable', 'Continuous variable']
    


    
#test = SuggestedFunction.suggested_html()
#print(test)

#SuggestedFunction.load_suggested(0,300,412)

