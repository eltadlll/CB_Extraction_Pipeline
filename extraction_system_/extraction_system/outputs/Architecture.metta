; ── Concept: Architecture ─────────────────────────────────────────
(Concept Architecture)
(Domain Architecture "Engineering")
(Description Architecture "Architecture is the art and science of designing and constructing buildings and other physical structures. It involves the creative process of conceptualizing spaces, considering their aesthetic appeal, functionality, structural integrity, and environmental impact, to create environments that serve human needs and enhance quality of life.")

(CorePredicate Architecture "designing")
(CorePredicate Architecture "constructing")
(CorePredicate Architecture "conceptualizing")

(ConceptWorldSpecs Architecture (WorldSpec-Engineering WorldSpec-Materials WorldSpec-Physics WorldSpec-SocialScience WorldSpec-Economics))

(: design-and-construction (Property Architecture))
(WorldSpecSet design-and-construction (WorldSpec-Engineering WorldSpec-Materials WorldSpec-Physics WorldSpec-SocialScience))
(Degree design-and-construction degree-1)
(CentralityValue design-and-construction 0.9500)
(Description design-and-construction "Architecture fundamentally involves the systematic process of designing and overseeing the construction of physical structures.")

(: space-conceptualization (Property Architecture))
(WorldSpecSet space-conceptualization (WorldSpec-Engineering WorldSpec-SocialScience WorldSpec-Cognition))
(Degree space-conceptualization degree-1)
(CentralityValue space-conceptualization 0.9000)
(Description space-conceptualization "A core aspect of architecture is the creative conceptualization of spaces to meet specific functional and aesthetic requirements.")

(: human-environment-creation (Property Architecture))
(WorldSpecSet human-environment-creation (WorldSpec-SocialScience WorldSpec-Ecology WorldSpec-Engineering WorldSpec-Economics))
(Degree human-environment-creation degree-1)
(CentralityValue human-environment-creation 0.8800)
(Description human-environment-creation "Architecture aims to create built environments that serve human needs, enhance quality of life, and interact with their surroundings.")

(: structural-integrity-assurance (Property Architecture))
(WorldSpecSet structural-integrity-assurance (WorldSpec-Engineering WorldSpec-Physics WorldSpec-Materials))
(Degree structural-integrity-assurance degree-2)
(CentralityValue structural-integrity-assurance 0.7000)
(Description structural-integrity-assurance "Ensuring the safety and stability of buildings through sound structural design is a critical responsibility in architecture.")

(: aesthetic-shaping (Property Architecture))
(WorldSpecSet aesthetic-shaping (WorldSpec-SocialScience WorldSpec-Cognition))
(Degree aesthetic-shaping degree-2)
(CentralityValue aesthetic-shaping 0.6500)
(Description aesthetic-shaping "Architecture involves shaping the visual and experiential qualities of structures to achieve aesthetic appeal and cultural significance.")

(: material-specification (Property Architecture))
(WorldSpecSet material-specification (WorldSpec-Materials))
(Degree material-specification degree-3)
(CentralityValue material-specification 0.4500)
(Description material-specification "The selection and specification of appropriate materials are crucial for a building's performance, durability, and appearance.")

(: regulatory-compliance (Property Architecture))
(WorldSpecSet regulatory-compliance (WorldSpec-Economics WorldSpec-SocialScience))
(Degree regulatory-compliance degree-4)
(CentralityValue regulatory-compliance 0.4000)
(Description regulatory-compliance "Architectural projects must adhere to various building codes, zoning laws, and environmental regulations.")

(: historical-documentation (Property Architecture))
(WorldSpecSet historical-documentation ())
(Degree historical-documentation degree-5)
(CentralityValue historical-documentation 0.1500)
(Description historical-documentation "Architectural works often serve as historical records, reflecting the societal values and technological capabilities of their time.")
