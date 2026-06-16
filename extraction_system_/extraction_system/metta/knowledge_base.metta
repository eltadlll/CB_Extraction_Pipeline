; ============================================================
; MeTTa Knowledge Base — Extraction System
; Hyperon / OpenCog Hyperon compatible
; ============================================================

; ─── Core types ──────────────────────────────────────────────
(: Concept Type)
(: Property Type)
(: WorldSpec Type)
(: Degree Type)

; ─── WorldSpec atoms ─────────────────────────────────────────
(: WorldSpec-Physics        WorldSpec)
(: WorldSpec-Chemistry      WorldSpec)
(: WorldSpec-Biology        WorldSpec)
(: WorldSpec-Ecology        WorldSpec)
(: WorldSpec-Thermodynamics WorldSpec)
(: WorldSpec-Engineering    WorldSpec)
(: WorldSpec-Mathematics    WorldSpec)
(: WorldSpec-ComputerScience WorldSpec)
(: WorldSpec-Economics      WorldSpec)
(: WorldSpec-SocialScience  WorldSpec)
(: WorldSpec-Philosophy     WorldSpec)
(: WorldSpec-Medicine       WorldSpec)
(: WorldSpec-Agriculture    WorldSpec)
(: WorldSpec-Energy         WorldSpec)
(: WorldSpec-Materials      WorldSpec)
(: WorldSpec-Information    WorldSpec)
(: WorldSpec-Cognition      WorldSpec)
(: WorldSpec-Linguistics    WorldSpec)

; ─── Degree atoms & ordering ─────────────────────────────────
(: degree-1 Degree)   ; 0.85–1.00 — core / definitional
(: degree-2 Degree)   ; 0.65–0.85 — strong
(: degree-3 Degree)   ; 0.45–0.65 — moderate
(: degree-4 Degree)   ; 0.25–0.45 — weak
(: degree-5 Degree)   ; 0.00–0.25 — peripheral / abstract

(= (degreeLT degree-5 degree-4) True)
(= (degreeLT degree-4 degree-3) True)
(= (degreeLT degree-3 degree-2) True)
(= (degreeLT degree-2 degree-1) True)

(= (degreeNumeric degree-1) 0.92)
(= (degreeNumeric degree-2) 0.75)
(= (degreeNumeric degree-3) 0.55)
(= (degreeNumeric degree-4) 0.35)
(= (degreeNumeric degree-5) 0.12)

; ─── Utility rules ───────────────────────────────────────────

; A property is grounded if its WorldSpecSet is non-empty
(= (isGrounded $prop)
   (let $ws (getWorldSpecSet $prop)
     (not (= $ws ()))))

; All grounded properties of a concept
(= (groundedProperties $concept)
   (let $props (getProperties $concept)
     (filter isGrounded $props)))

; Properties in a given degree tier
(= (propertiesAtDegree $concept $degree)
   (let $props (getProperties $concept)
     (filter (lambda $p (= (getDegree $p) $degree)) $props)))

; ─── Auto-generated concept atoms appended below this line ───
; (appended by algebraic_encoder.py after each extraction run)

; ── Jazz (auto-extracted) ──────────────────────────
; ── Concept: Jazz ─────────────────────────────────────────
(Concept Jazz)
(Domain Jazz "Arts")
(Description Jazz "Jazz is a music genre that originated in the African-American communities of New Orleans, United States, in the late 19th and early 20th centuries. It is characterized by improvisation, syncopation, polyrhythms, and a strong emphasis on swing and blues notes, often featuring a call-and-response pattern and a blend of African and European musical traditions, evolving into diverse subgenres and influencing global music.")

(CorePredicate Jazz "Improvisation")
(CorePredicate Jazz "Composition")
(CorePredicate Jazz "Performance")
(CorePredicate Jazz "Arrangement")
(CorePredicate Jazz "Listening")

(ConceptWorldSpecs Jazz (WorldSpec-SocialScience WorldSpec-Cognition WorldSpec-Information WorldSpec-Philosophy))

(: spontaneous-creation (Property Jazz))
(WorldSpecSet spontaneous-creation (WorldSpec-Cognition WorldSpec-SocialScience WorldSpec-Information WorldSpec-Philosophy))
(Degree spontaneous-creation degree-1)
(CentralityValue spontaneous-creation 0.9500)
(Description spontaneous-creation "Jazz is fundamentally characterized by the spontaneous creation of musical ideas during performance.")

(: rhythmic-complexity (Property Jazz))
(WorldSpecSet rhythmic-complexity (WorldSpec-Mathematics WorldSpec-Cognition WorldSpec-SocialScience WorldSpec-Information))
(Degree rhythmic-complexity degree-1)
(CentralityValue rhythmic-complexity 0.9000)
(Description rhythmic-complexity "Jazz incorporates intricate rhythmic structures, including syncopation, polyrhythms, and a distinctive swing feel.")

(: cultural-synthesis (Property Jazz))
(WorldSpecSet cultural-synthesis (WorldSpec-SocialScience WorldSpec-Philosophy WorldSpec-Information WorldSpec-Cognition))
(Degree cultural-synthesis degree-1)
(CentralityValue cultural-synthesis 0.8800)
(Description cultural-synthesis "Jazz emerged as a unique blend of African and European musical traditions, rooted in African-American communities.")

(: expressive-performance (Property Jazz))
(WorldSpecSet expressive-performance (WorldSpec-Cognition WorldSpec-SocialScience))
(Degree expressive-performance degree-2)
(CentralityValue expressive-performance 0.7000)
(Description expressive-performance "Jazz performances are highly expressive, aiming to evoke strong emotional experiences in both musicians and listeners.")

(: genre-evolution (Property Jazz))
(WorldSpecSet genre-evolution (WorldSpec-SocialScience WorldSpec-Information))
(Degree genre-evolution degree-2)
(CentralityValue genre-evolution 0.6500)
(Description genre-evolution "Jazz is a dynamic music genre that continuously evolves into diverse subgenres and influences global musical landscapes.")

(: interactive-dialogue (Property Jazz))
(WorldSpecSet interactive-dialogue (WorldSpec-SocialScience))
(Degree interactive-dialogue degree-3)
(CentralityValue interactive-dialogue 0.4500)
(Description interactive-dialogue "A common structural element in jazz is the call-and-response pattern, fostering musical dialogue.")

(: instrumental-medium (Property Jazz))
(WorldSpecSet instrumental-medium (WorldSpec-Physics))
(Degree instrumental-medium degree-4)
(CentralityValue instrumental-medium 0.3500)
(Description instrumental-medium "Jazz is primarily performed through a wide array of musical instruments, each contributing to the ensemble's sound.")

(: global-reach (Property Jazz))
(WorldSpecSet global-reach ())
(Degree global-reach degree-5)
(CentralityValue global-reach 0.2000)
(Description global-reach "Jazz has achieved significant global recognition and has influenced various music genres worldwide.")


; ── Architecture (auto-extracted) ──────────────────────────
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


; ── Machine Learning (auto-extracted) ──────────────────────────
; ── Concept: Machine Learning ─────────────────────────────────────────
(Concept MachineLearning)
(Domain MachineLearning "Computer Science")
(Description MachineLearning "Machine Learning is a subfield of artificial intelligence that focuses on developing algorithms and statistical models that enable computer systems to learn from data, identify patterns, and make decisions or predictions without being explicitly programmed for every task. It involves training models on large datasets to recognize complex relationships and generalize this knowledge to new, unseen data, thereby improving performance over time across various applications.")

(CorePredicate MachineLearning "learn from data")
(CorePredicate MachineLearning "identify patterns")
(CorePredicate MachineLearning "make decisions or predictions")

(ConceptWorldSpecs MachineLearning (WorldSpec-ComputerScience WorldSpec-Mathematics WorldSpec-Information WorldSpec-Engineering WorldSpec-Cognition))

(: data-driven-learning (Property MachineLearning))
(WorldSpecSet data-driven-learning (WorldSpec-ComputerScience WorldSpec-Information WorldSpec-Cognition WorldSpec-Mathematics))
(Degree data-driven-learning degree-1)
(CentralityValue data-driven-learning 0.9500)
(Description data-driven-learning "Machine Learning systems acquire knowledge and improve performance by processing and analyzing large datasets.")

(: pattern-identification (Property MachineLearning))
(WorldSpecSet pattern-identification (WorldSpec-ComputerScience WorldSpec-Information WorldSpec-Cognition WorldSpec-Mathematics))
(Degree pattern-identification degree-1)
(CentralityValue pattern-identification 0.9200)
(Description pattern-identification "The core function of Machine Learning is to detect and extract meaningful patterns and relationships within complex data.")

(: predictive-decision-making (Property MachineLearning))
(WorldSpecSet predictive-decision-making (WorldSpec-ComputerScience WorldSpec-Mathematics WorldSpec-Engineering WorldSpec-Information))
(Degree predictive-decision-making degree-1)
(CentralityValue predictive-decision-making 0.9000)
(Description predictive-decision-making "Machine Learning enables systems to forecast future outcomes or make autonomous decisions based on learned insights.")

(: algorithmic-foundation (Property MachineLearning))
(WorldSpecSet algorithmic-foundation (WorldSpec-ComputerScience WorldSpec-Mathematics))
(Degree algorithmic-foundation degree-2)
(CentralityValue algorithmic-foundation 0.7000)
(Description algorithmic-foundation "Machine Learning relies heavily on the design and application of various algorithms and statistical models to process data.")

(: performance-optimization (Property MachineLearning))
(WorldSpecSet performance-optimization (WorldSpec-ComputerScience WorldSpec-Engineering))
(Degree performance-optimization degree-2)
(CentralityValue performance-optimization 0.6500)
(Description performance-optimization "Machine Learning models continuously refine their performance and accuracy through iterative training and evaluation processes.")

(: resource-intensive (Property MachineLearning))
(WorldSpecSet resource-intensive (WorldSpec-ComputerScience))
(Degree resource-intensive degree-3)
(CentralityValue resource-intensive 0.4500)
(Description resource-intensive "Machine Learning tasks, especially training large models, typically demand substantial computational resources.")

(: knowledge-generalization (Property MachineLearning))
(WorldSpecSet knowledge-generalization (WorldSpec-Cognition))
(Degree knowledge-generalization degree-4)
(CentralityValue knowledge-generalization 0.4000)
(Description knowledge-generalization "Machine Learning models are designed to generalize insights from training data to make accurate predictions on novel, previously unencountered data.")

(: ethical-considerations (Property MachineLearning))
(WorldSpecSet ethical-considerations ())
(Degree ethical-considerations degree-5)
(CentralityValue ethical-considerations 0.1500)
(Description ethical-considerations "The deployment of Machine Learning systems raises important ethical questions regarding bias, privacy, and accountability.")


; ── Evolution (auto-extracted) ──────────────────────────
; ── Concept: Evolution ─────────────────────────────────────────
(Concept Evolution)
(Domain Evolution "Biology")
(Description Evolution "Evolution is the fundamental biological process by which heritable characteristics of biological populations change over successive generations. This process, driven by mechanisms such as mutation, natural selection, genetic drift, and gene flow, leads to the diversity of life on Earth, the adaptation of organisms to their environments, and the emergence of new species over vast spans of time.")

(CorePredicate Evolution "heritable characteristics change")
(CorePredicate Evolution "driven by mechanisms")
(CorePredicate Evolution "leads to diversity of life")

(ConceptWorldSpecs Evolution (WorldSpec-Biology WorldSpec-Ecology WorldSpec-Chemistry WorldSpec-Information))

(: heritable-trait-change (Property Evolution))
(WorldSpecSet heritable-trait-change (WorldSpec-Biology WorldSpec-Information WorldSpec-Chemistry WorldSpec-Ecology))
(Degree heritable-trait-change degree-1)
(CentralityValue heritable-trait-change 0.9500)
(Description heritable-trait-change "The fundamental process involves the alteration of heritable characteristics within populations across generations.")

(: mechanism-driven-process (Property Evolution))
(WorldSpecSet mechanism-driven-process (WorldSpec-Biology WorldSpec-Ecology WorldSpec-Information))
(Degree mechanism-driven-process degree-1)
(CentralityValue mechanism-driven-process 0.9000)
(Description mechanism-driven-process "Evolution is propelled by specific biological mechanisms including natural selection, mutation, genetic drift, and gene flow.")

(: biodiversity-adaptation-generation (Property Evolution))
(WorldSpecSet biodiversity-adaptation-generation (WorldSpec-Biology WorldSpec-Ecology WorldSpec-Information))
(Degree biodiversity-adaptation-generation degree-1)
(CentralityValue biodiversity-adaptation-generation 0.8800)
(Description biodiversity-adaptation-generation "The long-term outcome of evolution is the generation of diverse life forms and their adaptation to various environments.")

(: long-temporal-process (Property Evolution))
(WorldSpecSet long-temporal-process (WorldSpec-Biology WorldSpec-Ecology))
(Degree long-temporal-process degree-2)
(CentralityValue long-temporal-process 0.7000)
(Description long-temporal-process "Evolution typically unfolds over vast spans of time, often requiring many generations for significant changes to accumulate.")

(: population-level-change (Property Evolution))
(WorldSpecSet population-level-change (WorldSpec-Biology WorldSpec-Ecology))
(Degree population-level-change degree-2)
(CentralityValue population-level-change 0.6500)
(Description population-level-change "Evolutionary changes occur at the level of populations, not individual organisms, affecting their genetic makeup over time.")

(: genetic-variation-dependency (Property Evolution))
(WorldSpecSet genetic-variation-dependency (WorldSpec-Biology WorldSpec-Information))
(Degree genetic-variation-dependency degree-3)
(CentralityValue genetic-variation-dependency 0.5000)
(Description genetic-variation-dependency "Genetic variation within a population is a prerequisite for evolutionary change, providing the raw material for selection.")

(: environmental-interaction (Property Evolution))
(WorldSpecSet environmental-interaction (WorldSpec-Ecology))
(Degree environmental-interaction degree-4)
(CentralityValue environmental-interaction 0.4000)
(Description environmental-interaction "Organisms interact with their environment, which exerts selective pressures influencing the direction of evolutionary change.")

(: historical-record-formation (Property Evolution))
(WorldSpecSet historical-record-formation ())
(Degree historical-record-formation degree-5)
(CentralityValue historical-record-formation 0.1500)
(Description historical-record-formation "Evolution leaves a historical record in the form of fossils and genetic lineages, allowing for its study and reconstruction.")

