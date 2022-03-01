#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!/usr/bin/env python
# coding: utf-8

# In[396]:


#!/usr/bin/python
#
# SFS-A68 labels
#

from collections import namedtuple
from treelib import Node, Tree


#--------------------------------------------------------------------------------
# Definitions
#--------------------------------------------------------------------------------
# a label and all meta information
Label = namedtuple( 'Label' , [

    'name'        , # The descriptor of this label, e.g. "DiningRoom", "LivingRoom", ... .
                    # We utilize it to uniquely name a class
    
    'id'          , # An integer ID linked to this label.

    'color'       , # The color of this label
    
    ] )

class segmentation_data(object): 
        def __init__(self, id = None, color = None):
            self.id = id
            self.color = color


# In[13]:




GroundTruthLayoutElements = Tree()
GroundTruthLayoutElements.create_node("Root", "Space",
                                      data = segmentation_data())
GroundTruthLayoutElements.create_node("Category", "ResidentialSpace", parent='Space',
                                      data = segmentation_data())
GroundTruthLayoutElements.create_node("Subcategory", "CommunalSpace", parent='ResidentialSpace',
                                      data = segmentation_data())
GroundTruthLayoutElements.create_node("SpaceFunctionClass", "DiningRoom", parent='CommunalSpace',
                                      data = segmentation_data(1,'(107,74,101)'))
GroundTruthLayoutElements.create_node("SpaceFunctionClass", "FamilyRoom", parent='CommunalSpace',
                                      data = segmentation_data(2,'(166, 206, 227)'))
GroundTruthLayoutElements.create_node("SpaceFunctionClass", "LivingRoom", parent='CommunalSpace',
                                      data = segmentation_data(3,'(242, 0, 192)'))

GroundTruthLayoutElements.create_node("Subcategory", "PrivateSpace", parent='ResidentialSpace',
                                      data = segmentation_data())
GroundTruthLayoutElements.create_node("SpaceFunctionClass", "Bedroom", parent='PrivateSpace',
                                      data = segmentation_data(4,'(0, 255, 248)'))
GroundTruthLayoutElements.create_node("SpaceFunctionClass", "MasterBedroom", parent='Bedroom',
                                      data = segmentation_data(5,'(0,175,175)'))
GroundTruthLayoutElements.create_node("SpaceFunctionClass", "BoxRoom", parent='Bedroom',
                                      data = segmentation_data(6,'(4,72,148)'))
GroundTruthLayoutElements.create_node("SpaceFunctionClass", "HomeOffice", parent='PrivateSpace',
                                      data = segmentation_data(7,'(194, 123, 160)'))


GroundTruthLayoutElements.create_node("Category", "ServiceSpace", parent='Space',
                                      data = segmentation_data())
GroundTruthLayoutElements.create_node("SpaceFunctionClass", "Shaft", parent='ServiceSpace',
                                      data = segmentation_data(8,'(253, 237, 0)'))
GroundTruthLayoutElements.create_node("SpaceFunctionClass", "StorageRoom", parent='ServiceSpace',
                                      data = segmentation_data(9,'(255, 182, 0)'))
GroundTruthLayoutElements.create_node("SpaceFunctionClass", "WalkInCloset", parent='StorageRoom',
                                      data = segmentation_data(10,'(191, 144, 0)'))


GroundTruthLayoutElements.create_node("Subcategory", "SanitarySpace", parent='ServiceSpace',
                                      data = segmentation_data())
GroundTruthLayoutElements.create_node("SpaceFunctionClass", "Bathroom", parent='SanitarySpace',
                                      data = segmentation_data(11,'(255, 0, 0)'))
GroundTruthLayoutElements.create_node("SpaceFunctionClass", "Toilet", parent='SanitarySpace',
                                      data = segmentation_data(12,'(69, 129, 142)'))
GroundTruthLayoutElements.create_node("SpaceFunctionClass", "Kitchen", parent='SanitarySpace',
                                      data = segmentation_data(13,'(131, 126, 197)'))
GroundTruthLayoutElements.create_node("SpaceFunctionClass", "LaundryRoom", parent='SanitarySpace',
                                      data = segmentation_data(14,'(0, 0, 255)'))


GroundTruthLayoutElements.create_node("Category", "CirculationSpace", parent='Space',
                                      data = segmentation_data())
GroundTruthLayoutElements.create_node("Subcategory", "VerticalCirculationSpace", parent='CirculationSpace',
                                      data = segmentation_data())
GroundTruthLayoutElements.create_node("SpaceFunctionClass", "Elevator", parent='VerticalCirculationSpace',
                                      data = segmentation_data(15,'(9, 244, 156)'))
GroundTruthLayoutElements.create_node("SpaceFunctionClass", "Stairway", parent='VerticalCirculationSpace',
                                      data = segmentation_data(16,'(168, 134, 113)'))

GroundTruthLayoutElements.create_node("Subcategory", "HorizontalCirculationSpace", parent='CirculationSpace',
                                      data = segmentation_data())
GroundTruthLayoutElements.create_node("SpaceFunctionClass", "Entrance", parent='HorizontalCirculationSpace',
                                      data = segmentation_data(17,'(151, 143, 141)'))
GroundTruthLayoutElements.create_node("SpaceFunctionClass", "Hallway", parent='HorizontalCirculationSpace',
                                      data = segmentation_data(18,'(125, 62, 32)'))
GroundTruthLayoutElements.create_node("SpaceFunctionClass", "MainHallway", parent='Hallway',
                                      data = segmentation_data(19,'(225, 138, 96)'))
GroundTruthLayoutElements.create_node("SpaceFunctionClass", "InternalHallway", parent='Hallway',
                                      data = segmentation_data(20,'(155, 94, 65)'))

GroundTruthLayoutElements.create_node("Category", "ExternalSpace", parent='Space',
                                      data = segmentation_data())
GroundTruthLayoutElements.create_node("SpaceFunctionClass", "AccessBalcony", parent='ExternalSpace',
                                      data = segmentation_data(21,'(255, 255, 22)'))
GroundTruthLayoutElements.create_node("SpaceFunctionClass", "Loggia", parent='ExternalSpace',
                                      data = segmentation_data(22,'(120, 56, 145)'))


# In[399]:


### Layout element classes


InputLayoutElements = Tree()
InputLayoutElements.create_node("Root", "root", data = segmentation_data())
InputLayoutElements.create_node("Category", "Space", parent='root',
                                data = segmentation_data())
InputLayoutElements.create_node("SpaceElementClass", "InternalSpace",
                                parent='Space', data = segmentation_data(1,'(102,102,122)'))
InputLayoutElements.create_node("SpaceElementClass", "ExternalSpace",
                                parent='Space', data = segmentation_data(2,'(161,162,155)'))


InputLayoutElements.create_node("Category", "SpaceElement", parent='root',
                                data = segmentation_data())
InputLayoutElements.create_node("SubCategory", "SpaceContainedElement", parent='SpaceElement',
                                data = segmentation_data())

InputLayoutElements.create_node("SubSubCategory", "CirculationElement", parent='SpaceContainedElement',
                                data = segmentation_data())
InputLayoutElements.create_node("SpaceElementClass", "FlightOfStairs", parent='CirculationElement',
                                data = segmentation_data(3,'(230, 184, 175)'))
InputLayoutElements.create_node("SpaceElementClass", "Landing", parent='CirculationElement',
                                data = segmentation_data(4,'(102, 1, 30)'))

InputLayoutElements.create_node("SubSubCategory", "FurnishingElement", parent='SpaceContainedElement', 
                                data = segmentation_data())
InputLayoutElements.create_node("SpaceElementClass", "KitchenElement", parent='FurnishingElement',
                                data = segmentation_data(5,'(253, 223, 162)'))
InputLayoutElements.create_node("SpaceElementClass", "SanitaryElemen", parent='FurnishingElement',
                                data = segmentation_data(6,'(248, 193, 79)'))

InputLayoutElements.create_node("SubSubCategory", "EquipmentElement", parent='SpaceContainedElement',
                                data = segmentation_data())
InputLayoutElements.create_node("SubSubSubCategory", "HomeAppliance", parent='EquipmentElement', 
                                data = segmentation_data())
InputLayoutElements.create_node("SpaceElementClass", "TextileCareAppliance", parent='HomeAppliance',
                                data = segmentation_data(7,'(159, 140, 81)'))

InputLayoutElements.create_node("SubCategory", "SpaceEnclosingElement", parent='SpaceElement', 
                                data = segmentation_data())
InputLayoutElements.create_node("SpaceElementClass", "Opening", parent='SpaceEnclosingElement', 
                                data = segmentation_data(8,'(109, 189, 110)'))
InputLayoutElements.create_node("SpaceElementClass", "Partition", parent='SpaceEnclosingElement', 
                                data = segmentation_data(9,'(255, 107, 0)'))
InputLayoutElements.create_node("SpaceElementClass", "Window", parent='SpaceEnclosingElement', 
                                data = segmentation_data(10,'(200, 255, 0)'))
InputLayoutElements.create_node("SubSubCategory", "Door", parent='SpaceEnclosingElement', 
                                data = segmentation_data())
InputLayoutElements.create_node("SpaceElementClass", "RegularDoor", parent='Door', 
                                data = segmentation_data(11,'(0, 255, 0)'))
InputLayoutElements.create_node("SpaceElementClass", "UnitDoor", parent='Door', 
                                data = segmentation_data(12,'(72, 112, 39)'))
InputLayoutElements.create_node("SpaceElementClass", "ElevatorDoor", parent='Door', 
                                data = segmentation_data(13,'(187, 244, 154)'))






def find_tag(tree = InputLayoutElements, tag = 'SpaceElementClass'):
    #--------------------------------------------------------------------------------
    # A list of all labels
    #--------------------------------------------------------------------------------
    labels = [ ]
    nodes = [n for n in tree.all_nodes() if n.tag == tag ]
    for node in nodes:
        labels.append( Label(node.identifier, node.data.id, node.data.color))
        
    # name to label object
    name2label      = { label.name    : label for label in labels }
    return name2label


# In[402]:


def get_SpaceElementClasses():
    
    SpaceElementClassLabels = find_tag (InputLayoutElements, 'SpaceElementClass')
    
    return SpaceElementClassLabels


# In[403]:


def get_SpaceFunctionClasses():
        
    SpaceFunctionClassLabels = find_tag (GroundTruthLayoutElements, 'SpaceFunctionClass')
    
    return SpaceFunctionClassLabels


# In[404]:


if __name__ == "__main__":
    
    SpaceElementClassLabels = get_SpaceElementClasses()
    InputLayoutElements.show(idhidden=False,data_property="color")
        
    for key in SpaceElementClassLabels.keys():        
        print("SpaceElementId: {id}, name: {name}, color: {color}".format( name=key, id=SpaceElementClassLabels[key].id,  color=SpaceElementClassLabels[key].color))

    print()

    SpaceFunctionClassLabels = get_SpaceFunctionClasses()
    GroundTruthLayoutElements.show(idhidden=False,data_property="color")
    for key in SpaceFunctionClassLabels.keys():
        print("SpaceFunctionId: {id}, name: {name}, color: {color}".format( name=key, id=SpaceFunctionClassLabels[key].id,  color=SpaceFunctionClassLabels[key].color))
        

