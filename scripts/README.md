##README.md

The scripts folder contains:

install.py  = setup of local folders and config
example*.py = example scripts to show usage
collect*.py = downloads and extracts datasets to local lists

A sub folder scripts\_TO_PROCESS is used to store very large 
datasets downloaded by users to extract their own lists for
fast data generation.

##Ontologies

Examples of ontologies below are from http://www.acutesoftware.com.au/aikif/ontology.html

###WordNet
page = http://wordnet.princeton.edu/wordnet/download/
data = http://wordnetcode.princeton.edu/wn3.1.dict.tar.gz
Best word list, not in OWL format, though qualifies as an upper ontology by including the most general concepts as well as more specialized concepts, related to each other not only by the subsumption relations, but by other semantic relations as well, such as part-of and cause. However, unlike Cyc, it has not been formally axiomatized so as to make the logical relations between the concepts precise. It has been widely used in Natural language processing research

###OpenCyc
page = http://en.wikipedia.org/wiki/Cyc#OpenCyc
data = http://sourceforge.net/projects/texai/files/open-cyc-rdf/1.1/open-cyc.rdf.ZIP/download
Was proprietry, now open source. Fairly precise, this is the best bet for AI applications

###SUMO - Suggested Upper Merged Ontology
page = http://www.ontologyportal.org/
data = http://sigmakee.cvs.sourceforge.net/viewvc/sigmakee/KBs/?view=tar
Created by the IEEE working group P1600.1 - has multiple files by subject area which includes an upper ontology (which file?)
Sample file saved to S:\DATA\opendata\ontology\SUMO\KBs\Mid-level-ontology.kif (879,032 bytes)
47 files in folder, totalling 17,591,907 bytes

###DOLCE - Descriptive Ontology for Linguistic and Cognitive Engineering 
page = http://www.loa.istc.cnr.it/
data = http://www.loa-cnr.it/ontologies/DOLCE-Lite.owl
Not an active project on website, but has a clear cognitive bias, in that it aims at capturing the ontological categories underlying natural language and human common sense
Sample file saved to S:\DATA\opendata\ontology\DOLCE\DOLCE-Lite.owl (106,827 bytes)
10 files in folder, totalling 624,366 bytes

###DBPedia
page = http://wiki.dbpedia.org/Datasets
data = http://wiki.dbpedia.org/Downloads39
The most comprehensive set of data based on Wikipedia (470M facts)
Sample file saved to S:\DATA\opendata\ontology\wikipedia_categories\dbpedia-ontology.owl.bz2.owl.bz2.owl (259,244 bytes)
24 files in folder, totalling 2,414,659,446 bytes

###BFO - Basic Formal Ontology
page = http://www.ifomis.org/bfo
data = http://www.ifomis.org/bfo/1.1
Incorporates both three-dimensionalist and four-dimensionalist perspectives on reality within a single framework. Has over 100 other ontologies build based on this
Sample file saved to S:\DATA\opendata\ontology\BFO\bfo-1.1.owl (45,264 bytes)
7 files in folder, totalling 238,453 bytes

###UMBEL
page = http://umbel.org/
data = https://github.com/structureddynamics/UMBEL/archive/master.zip
Maps to a simplified subset of the OpenCyc ontology (28,000 entries)
Sample file saved to S:\DATA\opendata\ontology\UMBEL\umbel.n3 (505,824 bytes)
1 files in folder, totalling 505,824 bytes

###DnS - Descriptions and Situations (implementation of DOLCE+DnS-Ultralite abbreviated to DUL) 
page = http://stlab.istc.cnr.it/stlab/The_Semantic_Technology_Laboratory_%28STLab%29
data = http://www.ontologydesignpatterns.org/ont/dul/DUL.owl
constructivist ontology that pushes DOLCEs descriptive stance even further allowing for context-sensitive redescriptions of the types and relations postulated by other given ontologies
Sample file saved to S:\DATA\opendata\ontology\DnS\DUL.owl (244,258 bytes)
1 files in folder, totalling 244,258 bytes

###GFO - General Formal Ontology
page = http://www.onto-med.de/ontologies/index.jsp
data = http://www.onto-med.de/ontologies/gfo.owl
have developed a top level ontology and a biological core ontology. OWL file is copyright, but redistribution allowed
Sample file saved to S:\DATA\opendata\ontology\GFO\gfo-ato.owl (20,855 bytes)
9 files in folder, totalling 420,717 bytes

###UFO - Unified Foundation Ontology
page = https://oxygen.informatik.tu-cottbus.de/drupal7/ufo/
data = 
new, pretty good. tested for complex domains, combines DOLCE and GFO. Count not find single download OWL file
Not downloaded

###CIDOC Conceptual Reference Model
page = http://en.wikipedia.org/wiki/CIDOC_Conceptual_Reference_Model
data = http://www.cidoc-crm.org/rdfs/cidoc_crm_v5.0.4_official_release.rdfs
provides an extensible ontology for concepts and information in cultural heritage and museum documentation. Includes its own version of an upper ontology in its core classes
Sample file saved to S:\DATA\opendata\ontology\CIDOC\cidoc_crm_v5.0.4_official_release.rdfs (307,674 bytes)
1 files in folder, totalling 307,674 bytes

###COSMO - COmmon Semantic MOdel
page = http://ontolog.cim3.net/cgi-bin/wiki.pl?COSMO
data = http://www.micra.com/COSMO/COSMO.owl
The current (May 2009) OWL version of COSMO has over 6400 types (OWL classes), over 700 relations, and over 1400 restrictions
Sample file saved to S:\DATA\opendata\ontology\COSMO\COSMO.owl (10,036,090 bytes)
6 files in folder, totalling 16,015,894 bytes

###YAMATO - Yet Another More Advanced Top Ontology
page = http://www.ei.sanken.osaka-u.ac.jp/hozo/onto_library/upperOnto.htm
data = http://www.ei.sanken.osaka-u.ac.jp/hozo/onto_library/download.php?filename=YAMATO20120714owl.zip
complex but very advanced
Sample file saved to S:\DATA\opendata\ontology\YAMATO\YAMATO20120714.owl (530,486 bytes)
3 files in folder, totalling 1,448,966 bytes

###PROTON
page = http://www.ontotext.com/proton-ontology
data = http://www.ontotext.com/sites/default/files/proton/protontop.ttl
basic subsumption hierarchy which provides coverage of most of the upper-level concepts necessary for semantic annotation, indexing, and retrieval
Sample file saved to S:\DATA\opendata\ontology\PROTON\protontop.ttl (40,080 bytes)
2 files in folder, totalling 230,791 bytes

###IDEAS
page = http://www.ideasgroup.org/7Documents/
data = http://www.ideasgroup.org/file_download/5/IDEAS+Foundation+v1_0+Released+2009-04-24.xmi.zip
The most common usage of IDEAS will be in direct exchange of information between architectural modelling tools are repositories
Sample file saved to S:\DATA\opendata\ontology\IDEAS\IDEAS Foundation v1_0 Released 2009-04-24.xmi (3,073,554 bytes)
2 files in folder, totalling 7,319,058 bytes

###MarineTLO
page = http://www.ics.forth.gr/isl/MarineTLO/
data = http://www.ics.forth.gr/isl/MarineTLO/v3/core_v3.owl
MarineTLO is a top-level ontology for the marine domain (also applicable to the terrestrial domain)
Sample file saved to S:\DATA\opendata\ontology\MarineTLO\core_v3.owl (21,541 bytes)
2 files in folder, totalling 49,107 bytes
