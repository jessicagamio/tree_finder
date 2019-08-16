
from sqlalchemy import func
from model import TreeSpecies,Tree,connect_to_db, db
from server import app
import json

if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()


def create_species():
    """create tree_species table"""
    tree_species = {}

    # Create TreeSpecies
    scientific_name = 'Platanus x hispanica'
    common_name = 'Sycarmore'
    shape = 'palmate'
    margin = 'entire'
    venation = 'pinnate'
    factoid = 'Dicidous Tree. Bare through November-March. Member of the Sycamore Family'
    image = '/static/img/platanus_x_hispanica.jpg'
    platanus_x_hispanica = TreeSpecies(sci_name=scientific_name, 
                common_name=common_name,
                shape=shape, 
                factoid=factoid, 
                margin=margin, 
                venation=venation, 
                image=image)
    db.session.add(platanus_x_hispanica)
    db.session.commit()
    tree_species[scientific_name] = platanus_x_hispanica


    scientific_name = 'Magnolia grandiflora'
    common_name= 'Magnolia'
    shape = 'obtuse'
    margin = 'entire'
    venation = 'pinnate'
    factoid = 'facts'
    image = 'an_image'
    Magnolia_grandiflora = TreeSpecies(sci_name=scientific_name, 
                common_name=common_name,
                shape=shape, 
                factoid=factoid, 
                margin=margin, 
                venation=venation, 
                image=image)
    db.session.add(Magnolia_grandiflora)
    db.session.commit()
    tree_species[scientific_name]= Magnolia_grandiflora


    scientific_name = 'Prunus cerasifera'
    common_name = 'cherry plum'
    shape = 'obtuse'
    margin = 'serrated'
    venation = 'venation'
    factoid = 'facts'
    image = 'an_image'
    Prunus_cerasifera = TreeSpecies(sci_name=scientific_name, 
                common_name=common_name,
                shape=shape, 
                factoid=factoid, 
                margin=margin, 
                venation=venation, 
                image=image)
    db.session.add(Prunus_cerasifera)
    db.session.commit()
    tree_species[scientific_name]= Prunus_cerasifera


    scientific_name = 'Tristaniopsis laurina'
    common_name = 'common name'
    shape = 'obtuse'
    margin = 'entire'
    venation = 'venation'
    factoid = 'facts'
    image = 'an_image'
    Tristaniopsis_laurina = TreeSpecies(sci_name=scientific_name, 
                common_name=common_name,
                shape=shape, 
                factoid=factoid, 
                margin=margin, 
                venation=venation, 
                image=image)
    db.session.add(Tristaniopsis_laurina)
    db.session.commit()
    tree_species[scientific_name]=Tristaniopsis_laurina

            
    scientific_name = "Ficus microcarpa nitida 'Green Gem'"
    common_name= 'common_name'
    shape = 'obtuse'
    margin = 'entire'
    venation = 'pinnate'
    factoid = 'facts'
    image = 'an_image'
    Ficus_microcarpa_nitida = TreeSpecies(sci_name=scientific_name, 
                common_name=common_name,
                shape=shape, 
                factoid=factoid, 
                margin=margin, 
                venation=venation, 
                image=image)
    db.session.add(Ficus_microcarpa_nitida)
    db.session.commit()
    tree_species[scientific_name]= Ficus_microcarpa_nitida

    return tree_species

def create_trees(tree_species):
    """create trees table"""
    TREE_DATA = "trees_sf/rows.json"

    trees_json = open(TREE_DATA).read()

    tree_info = json.loads(trees_json)

    entries = tree_info['data'].__len__()


    for i in range(entries):

        tree_type =tree_info['data'][i][10]

        # split out the scientific and common name from data
        scientific_name, common_name = tree_type.split('::')
        scientific_name = scientific_name.strip()

        latitude = tree_info['data'][i][23]
        longitude = tree_info['data'][i][24] 

        if latitude == None or longitude == None or scientific_name not in ['Platanus x hispanica','Magnolia grandiflora','Prunus cerasifera','Tristaniopsis laurina',"Ficus microcarpa nitida 'Green Gem'"]:
            continue

        tree = Tree(lat= float(latitude), lon= float(longitude), tree_species= tree_species[scientific_name])

        db.session.add(tree)


tree_species = create_species()
create_trees(tree_species)
db.session.commit()



