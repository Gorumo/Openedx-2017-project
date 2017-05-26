from SPARQLWrapper import SPARQLWrapper, JSON, XML, N3, RDF
import json

concepts={}
sparql_select = SPARQLWrapper("http://127.0.1.1:8080/rdf4j-server/repositories/1")
sparql_select.setReturnFormat(JSON)
select_start="""select ?html where { ?unit_url <http://www.semanticweb.org/EdxOntology/Main#consistsOf> ?html filter (contains(str(?unit_url), '"""
select_what = "4c42451cbea84fe99bd6f6d7836b9100"
select_end="'))}"
sparql_select.setQuery(select_start+select_what+select_end)
results = sparql_select.query()
res = results.convert()
for result in res["results"]["bindings"]:
    html_id=result["html"]["value"].split("#")
# html_id[1]

select_start="""select ?concept_url where { ?html <http://www.semanticweb.org/EdxOntology/Main#hasConcept> ?concept_url filter (contains(str(?html), '"""
select_what = html_id[1]
select_end="'))}"

sparql_select.setQuery(select_start+select_what+select_end)
results = sparql_select.query()
res = results.convert()
for result in res["results"]["bindings"]:
    concept_id=result["concept_url"]["value"]
    select_start="""select ?concept where { ?concept_url rdfs:label ?concept filter (contains(str(?concept_url), '"""
    select_what = concept_id
    select_end="'))}"
    sparql_select.setQuery(select_start+select_what+select_end)
    results = sparql_select.query()
    res = results.convert()
    for result in res["results"]["bindings"]:
        concept_label=result["concept"]["value"]
        #print result["concept"]["value"]
    
    select_start="""PREFIX Main: <http://www.semanticweb.org/EdxOntology/Main#> select ?unit where { ?unit Main:hasConcept ?concept filter (contains(str(?concept), '"""
    select_what = concept_id
    select_end="'))}"
    sparql_select.setQuery(select_start+select_what+select_end)
    results = sparql_select.query()
    res = results.convert()
    concept_units=[]
    for result in res["results"]["bindings"]:
        unit_id=result["unit"]["value"].split("#")[1]
        if unit_id!=html_id[1]:
            #course_name = res["results"]["bindings"][0]["url"]["value"]
            select_start="""PREFIX Main: <http://www.semanticweb.org/EdxOntology/Main#> select ?vertical
where { ?vertical Main:consistsOf ?unit filter (contains(str(?unit), '"""
            select_what = unit_id
            select_end="'))}"
            sparql_select.setQuery(select_start+select_what+select_end)
            results = sparql_select.query()
            res = results.convert()
            for result in res["results"]["bindings"]:
                #course_name=unicode(getattr(self.runtime, 'course_id', 'course_id'))
                select_start="""PREFIX Main: <http://www.semanticweb.org/EdxOntology/Main#> select ?url where { ?course rdf:type Main:Course. ?course Main:consistsOf ?chapters. ?course <http://www.w3.org/1999/02/22-rdf-syntax-ns#Alt> ?url. ?chapters Main:consistsOf ?seq. ?seq Main:consistsOf ?vertical. filter (contains(str(?vertical), '"""
                vert_id=result["vertical"]["value"].split("#")[1]
                print vert_id
                select_what = vert_id
                select_end="'))}"
                sparql_select.setReturnFormat(JSON)
                sparql_select.setQuery(select_start+select_what+select_end)
                main_c = sparql_select.query()
                main = main_c.convert()
                course_name=main["results"]["bindings"][0]["url"]["value"]
                concept_units.append("http://192.168.33.10/courses/"+course_name+"/jump_to/block-v1:"+course_name+"+type@vertical+block@"+vert_id)
    concepts[concept_label]=concept_units
print concepts