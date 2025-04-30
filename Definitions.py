import random
definitions = {
    "acceptable identification": "(a) in the case of a person, a temporary identity certificate, an identity document or identity card issued in terms of the Identification Act, 1997 (Act No. 68 of 1997); (b) in the case of a person, a valid South African passport issued to a South African citizen; (c) in the case of a person not permanently resident in the Republic, an identity document issued by a foreign country or a traffic register number certificate issued in terms of regulation 335; (c) in the case of a person, a driving licence card issued in terms of regulation 108.",
    "articulated motor vehicle": "a combination of motor vehicles consisting of a truck-tractor and a semi-trailer.",
    "bridge": "includes a culvert and a causeway.",
    "bus": "a motor vehicle designed or adapted for the conveyance of more than 16 persons (including the driver, if any).",
    "combination of motor vehicles": "two or more motor vehicles coupled together.",
    "cross": "to move on a public road in a direction, which intersects the normal course of travel of traffic on such road.",
    "dedicated lane": "a portion of the public road reserved during certain period for the exclusive use of a certain categories of motor vehicles, the use and the categories of vehicles of which are prescribed by an appropriate sign.",
    "direction indicator": "a device fitted to a motor vehicle for the purpose of enabling the driver of such motor vehicle to intimate his or her intention to change the direction of travel of such motor vehicle to the right or to the left.",
    "DLTC": "driving licence testing centre, which is registered according to the National Road Traffic Act (93 of 1996).",
    "drawing": "drawing a vehicle designed or adapted solely for the purpose of being drawn, by a motor vehicle that is designed or adapted solely for the purpose of drawing such vehicle.",
    "driver": "any person who drives or attempts to drive any vehicle or who rides or attempts to ride any pedal cycle or who leads any draught, pack or saddle animal or herd or flock of animals, and 'drive' or any like word has a corresponding meaning.",
    "driving licence card": "a driving licence card issued in terms of the Act.",
    "driving time": "any period of time that the driver of a motor vehicle contemplated in the regulations occupies the drivers’ seat of such motor vehicle, whilst such motor vehicle is being operated on a public road or occupies the drivers’ seat of such motor vehicle, whilst the engine is running.",
    "edge of the roadway": "the boundary between the roadway and the shoulder, which is indicated by an appropriate road traffic sign, or in the absence of such sign— (a) in the case of a road with a bituminous or concrete surface, the edge of such surface; or (b) in the case of any other road, the edge of the improved part of the road intended for vehicular use.",
    "emergency brake": "a brake, other than a service brake, which can stop a vehicle.",
    "freeway": "a public road or a section of a public road, which has been designated as a freeway by an appropriate road traffic sign.",
    "front end": "in relation to— (a) a vehicle, other than a semi-trailer, means that part of the vehicle which projects furthest forward; or (b) a semi-trailer, means a line running parallel with the centre-line of the kingpin and connecting the sides of the semi-trailer at the widest and furthest point in front of the kingpin.",
    "goods": "any movable property.",
    "goods vehicle": "a motor vehicle, other than a motorcycle, motor tricycle, motor quadrucycle, motorcar, minibus or bus, designed or adapted for the conveyance of goods on a public road and includes a truck-tractor, adaptor dolly, converter dolly and breakdown vehicle. Note that Truck-tractor, Breakdown vehicle, Converter dolly, Adopter dolly are by definition goods vehicles.",
    "gross combination mass (GCM)": "in relation to a motor vehicle which is used to draw any other motor vehicle, means the maximum mass of any combination of motor vehicles, including the drawing vehicle, and load as specified by the manufacturer thereof or, in the absence of such specification, as determined by the registering authority.",
    "gross vehicle mass (GVM)": "in relation to a motor vehicle, means the maximum mass of such vehicle and its load as specified by the manufacturer thereof or, in the absence of such specification, as determined by the registering authority.",
    "haulage tractor": "a motor vehicle, designed or adapted mainly for drawing other vehicles, and with a gross combination mass exceeding 24 000kg, but does not include a truck-tractor or tractor.",
    "instructor": "any person who for direct reward— (a) instructs any other person in the driving of a motor vehicle; (b) teaches any other person the rules of the road or road traffic signs in order to obtain a learner’s or a driving licence.",
    "intersection": "the area embraced within the prolongation of the lateral boundary lines of two or more public roads, open to vehicular traffic, that join one another at any angle, whether or not one such public road crosses the other.",
    "junction": "that portion of an intersection contained within the prolongation of the lateral limits of the intersecting roadways and includes any portion of the roadway between such lateral limits, and any stop or yield line marking which is painted at such intersection.",
    "kerb line": "the boundary between the shoulder and the verge or, in the absence of a shoulder, the part between the edge of the roadway and the verge.",
    "licence disc": "a disc issued in terms of the Act that licenced a vehicle to be used on a public road and is only valid for 12 months.",
    "medical practitioner": "any person registered as such in terms of the Medical, Dental and Supplementary Health Service Professions Act, 1974 (Act No. 56 of 1974).",
    "midibus": "a sub-category of a bus, designed or modified solely or principally for the conveyance of more than 16 and not more than 35 persons (including the driver).",
    "minibus": "a motor vehicle designed or adapted solely or principally for the conveyance of more than nine, but not more than 16 persons, including the driver.",
    "motor car": "a motor vehicle, other than a motorcycle, motor tricycle or motor quadrucycle, designed or adapted solely or principally for the conveyance of not more than nine persons, including the driver.",
    "motorcycle": "a motor vehicle that has two wheels and includes any such vehicle having a sidecar attached.",
    "motor quadrucycle": "a motor vehicle, other than a tractor, which has four wheels and which is designed to be driven by the type of controls usually fitted to a motorcycle.",
    "motor tricycle": "a motor vehicle, other than a motorcycle or a tractor, which has three wheels and which is designed to be driven by the type of controls usually fitted to a motorcycle.",
    "motor vehicle": "any self-propelled vehicle and includes— (a) a trailer; and (b) a vehicle having pedals and an engine or an electric motor as an integral part thereof or attached thereto and which is designed or adapted to be propelled by means of such pedals, engine or motor, or both such pedals and engine or motor, but does not include— (i) any vehicle propelled by electrical power derived from storage batteries and which is controlled by a pedestrian; or (ii) any vehicle with a mass not exceeding 230 kilograms and specially designed and constructed, and not merely adapted, for the use of any person suffering from some physical defect or disability and used solely by such person.",
    "number plate": "a prescribed plate on which the licence number of a motor vehicle or motor trade number is displayed.",
    "operate on a public road": "to use or drive a vehicle or to permit a vehicle to be used or driven on a public road, or to have or to permit a vehicle to be on a public road.",
    "owner": "in relation to a vehicle, means— (a) the person who has the right to the use and enjoyment of a vehicle in terms of the common law or a contractual agreement with the title holder of such vehicle; (b) any person referred to in paragraph (a), for any period during which such person has failed to return that vehicle to the title holder in accordance with the contractual agreement referred to in paragraph (a); or (c) a motor dealer who is in possession of a vehicle for the purpose of sale, and who is licensed as such or obliged to be licensed in accordance with the regulations made under section 4, and ‘owned’ or any like word has a corresponding meaning.",
    "overall length": "in relation to a vehicle, means the distance between the front end and the rear end of the vehicle and, in relation to a combination of vehicles, the distance between the front end of the leading vehicle and the rear end of the rearmost vehicle.",
    "overall height": "in relation to a vehicle, means the distance measured from ground level to the highest part of— any part of such vehicle; or any load thereon, whichever part is the highest but, in the case of a vehicle driven by electrical power, the overall height does not include any overhead electrical contacting gear or catwalk protruding above such vehicle.",
    "overall width": "in relation to a vehicle, means the width measured between two planes parallel to the longitudinal centre-line of the vehicle and passing through the extreme projecting points on either side of such vehicle, excluding any side mirror or direction indicator or 30 millimetres on either side in respect of the fitment of air deflectors, reflectors or dangerous goods placards.",
    "park": "to keep a vehicle, whether occupied or not, stationary for a period of time longer than is reasonably necessary for the actual loading or unloading of persons or goods, but does not include any such keeping of a vehicle by reason of a cause beyond the control of the person in charge of such vehicle.",
    "parking brake": "a brake, normally a hand brake, used in the ordinary course of events to keep a vehicle stationary.",
    "pedestrian crossing": " (a) any portion of a public road designated as a pedestrian crossing by an appropriate road traffic sign; or (b) that portion of a public road at an intersection included within the prolongation or connection of the kerb line and adjacent boundary line of such road, when no pedestrian crossing has been designated by appropriate road traffic sign.",
    "public road": "any road, street or thoroughfare or any other place (whether a thoroughfare or not) which is commonly used by the public or any section thereof or to which the public or any section thereof has a right of access, and includes— (a) the verge of any such road, street or thoroughfare; (b) any bridge, ferry or drift traversed by any such road, street or thoroughfare; and (c) any other work or object forming part of or connected with or belonging to such road, street or thoroughfare. (Note: For the purpose of this document a 'road' refers to a public road).",
    "professional driver": "the driver of a motor vehicle, which drive a motor vehicle of a prescribed class; No person shall drive a motor vehicle of a prescribed class on a public road except in accordance with the conditions of a professional driving permit issued to him or her and unless he or she keeps such permit with him or her in the vehicle: Provided that this shall not apply to the holder of a learner’s licence who drives such vehicle while he or she is accompanied by a person registered as a professional driver in respect of that class of vehicle.",
    "rear end": "in relation to a vehicle, means that part of the vehicle which projects furthest to the rear.",
    "retro-reflector": "a reflector which complies with the standard specification SABS 513 'Retroreflectors (reflex reflectors)', and which bears a certification mark or an approval mark, but where a reflector is incorporated in a cluster of lamps, the certification or approval mark can be on the cluster instead of the reflector.",
    "road traffic sign": "a road traffic sign for the purpose of prohibiting, limiting, regulating or controlling traffic in general or any particular class of traffic on a public road or a section thereof.",
    "roadway": "that portion of a road, street or thoroughfare improved, constructed or intended for vehicular traffic, which is between the edges of the roadway.",
    "roadworthy": "in relation to a vehicle, means a vehicle, which complies with the relevant provisions of this Act and is otherwise in a fit condition to be operated on a public road.",
    "semi-trailer": "a trailer having no front axle and so designed that at least 15 per cent of its tare is super-imposed on and borne by a vehicle drawing such trailer.",
    "service brake": "a brake, normally a footbrake, used in the ordinary course of events to reduce the speed of a vehicle or to stop the vehicle.",
    "shoulder": "that portion of a road, street or thoroughfare between the edge of the roadway and the kerb line.",
    "sidewalk": "that portion of a verge intended for the exclusive use of pedestrians.",
    "stop": "the bringing to a standstill of a vehicle by the driver thereof.",
    "stop lamp": "a device fitted to a vehicle for the purpose of signalling, by means of a light, the intention of the driver of such vehicle to stop or reduce the speed of such vehicle.",
    "tare": "in relation to a motor vehicle, means the mass of such vehicle ready to travel on a road and includes the mass of— (a) any spare wheel and of all other accessories and equipment supplied by the manufacturer as standard for the particular model of motor vehicle concerned; (b) anything, which is a permanent part of the structure of such vehicle; (c) anything attached to such vehicle so as to form a structural alteration of a permanent nature; and (d) the accumulators, if such vehicle is self-propelled by electrical power, but does not include the mass of— (i) fuel; and (ii) anything attached to such vehicle, which is not of the nature referred to in paragraph (b) or (c).",
    "the Act": "the National Road Traffic Act, 1996 (Act No. 93 of 1996).",
    "towing": "towing a vehicle that is not designed or adapted for the purpose of being drawn.",
    "traffic island": "a physical island that serves as a channelizing device within a junction or on a public road.",
    "traffic lane": "a longitudinal division of a public road of sufficient width to accommodate the passage of a single line of vehicles.",
    "traffic signal": "a road traffic sign, which, by means of automatic light signals, alternately directs traffic to stop and permits it to proceed.",
    "tractor": "a motor vehicle designed or adapted mainly for drawing other vehicles and with a gross combination mass not exceeding 24 000kg, but does not include a truck-tractor.",
    "trailer": "a vehicle which is not self-propelled and which is designed or adapted to be drawn by a motor vehicle, but does not include a side-car attached to a motorcycle.",
    "truck-tractor": "a motor vehicle designed or adapted— (a) for drawing other vehicles; and (b) not to carry any load other than that imposed by a semi-trailer or by ballast, but does not include a tractor or a haulage tractor.",
    "urban area": "that portion of the area of jurisdiction of a local authority, which has by actual survey been subdivided into erven or is surrounded by surveyed erven, and includes the public roads abutting thereon.",
    "vehicle": "a device designed or adapted mainly to travel on wheels or crawler tracks and includes such a device which is connected with a draw-bar to a breakdown vehicle and is used as part of the towing equipment of a breakdown vehicle to support any axle or all the axles of a motor vehicle which is being salvaged other than such a device which moves solely on rails.",
    "verge": "that portion of a road, street or thoroughfare, including the sidewalk, which is not the roadway or the shoulder.",
    "LMV": "Light Motor Vehicle of which the Tare/Gross Vehicle Mass shall not be more than 3500 kg.",
    "HMV": "all Heavy Motor Vehicle of which: the T (Tare) exceeds 3500 kg; a minibus, a bus or a goods vehicle GVM (gross vehicle mass) exceeds 3500 kg; articulated vehicle and combinations of vehicles of which GCM (gross combination mass) of the drawing vehicle exceeds 3500 kilograms and combinations of vehicles of which the (GVM) of the trailer exceed 750kg.",
    "MC": "Motorcycle that includes a motorcycle, tricycle and quadrucycle."
}


term_list = list(definitions.keys())
random.shuffle(term_list)
print(term_list)

score = 0

for term in term_list:
    definition = definitions[term]
    print(f"What is the definition of: '{term}'?")
    user_answer = input("Your answer: ")
    print(f"The correct definition is: {definition}\n")
print(definitions) #Prints out the definition once you have answered a question
