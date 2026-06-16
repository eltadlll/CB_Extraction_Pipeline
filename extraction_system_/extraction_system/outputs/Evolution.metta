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
