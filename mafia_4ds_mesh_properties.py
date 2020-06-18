import bpy

from bpy import props
from bpy import types
from bpy import utils


class Mafia4ds_GlobalMeshProperties(types.PropertyGroup):
    Type : props.EnumProperty(
        name = "Type",
        items = [
            ("0x01", "Visual", ""),
            ("0x05", "Sector", ""),
            ("0x06", "Dummy",  ""),
            ("0x07", "Target", ""),
            ("0x0a", "Joint",  "")
        ]
    )
    
    VisualType : props.EnumProperty(
        name = "VisualType",
        items = [
            ("0x00", "Mesh",        ""),
            ("0x02", "SingleMesh",  ""),
            ("0x03", "SingleMorph", ""),
            ("0x04", "Billboard",   ""),
            ("0x05", "Morph",       ""),
            ("0x06", "Glow",        ""),
            ("0x08", "Mirror",      "")
        ]
    )
    
    Parameters : props.StringProperty(name = "Parameters")


class Mafia4ds_MeshProperties(types.Panel):
    "Mafia 4ds Mesh Properties"
    bl_label       = "Mafia 4ds Mesh Properties"
    bl_idname      = "OBJECT_PT_mafia_4ds_mesh_properties"
    bl_space_type  = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context     = "object"
    
    
    def draw(self, context):
        meshProps = context.object.MeshProps
        layout    = self.layout
        
        row = layout.row()
        layout.prop(meshProps, "Type")
        layout.prop(meshProps, "VisualType")
        layout.prop(meshProps, "Parameters")


def register():
    utils.register_class(Mafia4ds_GlobalMeshProperties)
    utils.register_class(Mafia4ds_MeshProperties)
    
    types.Object.MeshProps = props.PointerProperty(type = Mafia4ds_GlobalMeshProperties)


def unregister():
    utils.unregister_class(Mafia4ds_GlobalMeshProperties)
    utils.unregister_class(Mafia4ds_MeshProperties)
    
    del types.Scene.Aaa


if __name__ == "__main__":
    register()
