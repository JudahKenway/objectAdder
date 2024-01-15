bl_info = {
    "name" : "Object Adder", 
    "author": "User", 
    "version" : (1, 0),
    "blender": (4, 0, 1),
    "location" : "View3d > Tool", 
    "warning" : "", 
    "wiki_url" :"", 
    "catagory" : "Add Mesh", 
}
import bpy 

class TestPanel(bpy.types.Panel): #creating a class and giving it properties like name and type 
    bl_label = "Test Panel" #name of drop down panel 
    bl_idname = "PT_TestPanel" #desicnaiton of panel 
    bl_space_type = 'VIEW_3D' #what kind of add on 
    bl_region_type = 'UI' # wher is it located 
    bl_category = 'My 1st Addon' #name on list of options 
    
    def draw(self, context): # creating a function for class 
        layout = self.layout
        
        row = layout.row() #adds a row underneath Test Panel
        row.label(text = "Add an object", icon = 'CUBE') #telling function to show text
        row = layout.row()
        row.operator("mesh.primitive_cube_add", icon = 'MESH_CUBE')#tell panel how it is layed out
        row = layout.row()
        row.operator("mesh.primitive_uv_sphere_add", icon = 'MESH_UVSPHERE')
        row = layout.row()
        row.operator("object.text_add", icon =  'FILE_TEXT')
        row = layout.row()
        row.operator("mesh.primitive_plane_add", icon = 'MESH_PLANE')
        row = layout.row()
        row.operator("mesh.primitive_circle_add", icon = 'MESH_CIRCLE')
        row = layout.row()
        row.operator("mesh.primitive_ico_sphere_add", icon = 'MESH_ICOSPHERE')
        row = layout.row()
        row.operator("mesh.primitive_cylinder_add", icon = 'MESH_CYLINDER')
        row = layout.row()
        row.operator("mesh.primitive_cone_add", icon = 'MESH_CONE')
        row = layout.row()
        row.operator("mesh.primitive_torus_add", icon = 'MESH_TORUS')
        row = layout.row()
        row.operator("mesh.primitive_grid_add", icon = 'MESH_GRID')
        row = layout.row()
        row.operator("mesh.primitive_monkey_add", icon = 'MESH_MONKEY')

class PanelA(bpy.types.Panel):
    bl_label = "Panel A"
    bl_idname = "PT_PanelA"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'My 1st Addon'
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row() 
