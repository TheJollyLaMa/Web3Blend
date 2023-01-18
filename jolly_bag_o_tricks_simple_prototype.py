bl_info = {
    "name": "Object Adder",
    "author": "TheJollyLaMa",
    "version": (1,0),
#    "blender": (3.3.0,0),
    "location": "View3d > Tool",
    "warning": "",
    "wiki_url": "",
    "category": "Add Mesh"
}

import bpy
import requests
import json

class PANEL_PT_TestPanel(bpy.types.Panel):
    bl_label = "Jolly\'s Bag \'O Tricks"
    bl_idname = "PANEL_PT_TestPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jolly\'s Bag \'O Tricks'
    
    def draw(self, context):
        layout = self.layout
        
        # post to Minds
        row2 = layout.row()
        row2.label(text="MINDS", icon="OUTLINER_DATA_LIGHT")
        row2.operator(MindsOperator.bl_idname, text=MindsOperator.bl_label)

        # Spawn monkey
        row6 = layout.row()
        row6.label(text="MONKEY", icon="MONKEY")
        row6.operator(MonkeyOperator.bl_idname, text=MonkeyOperator.bl_label)
    

class MindsOperator(bpy.types.Operator):
    """Post creation to Minds social media platform"""
    bl_idname = "object.minds_operator"
    bl_label = "Send to Minds"    
    def post(self):
        pass
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        print("Follow the White Rabbit to Minds")
        try:
            self.post()
        except Exception as e:
            print(e)
            
        return {'FINISHED'}


class MonkeyOperator(bpy.types.Operator):
    """Spawns a monkey"""
    bl_idname = "object.monkey_operator"
    bl_label = "Spawn Monkey"
    
    def spawn(self):
        # add cube for the body core
        bpy.ops.mesh.primitive_cube_add()
        bpy.ops.transform.resize(value=(1.2,0.8,1.5))

        # add monkey head
        bpy.ops.mesh.primitive_monkey_add()
        bpy.ops.transform.translate(value=(0,-0.3,2))

        # add limbs
        bpy.ops.mesh.primitive_cylinder_add()
        bpy.ops.transform.translate(value=(2,0,0))
        bpy.ops.transform.resize(value=(0.5,0.5,1.5))
        bpy.ops.transform.rotate(value=0.523599, orient_axis='Y')

        bpy.ops.mesh.primitive_cylinder_add()
        bpy.ops.transform.translate(value=(-2,0,0))
        bpy.ops.transform.resize(value=(0.5,0.5,1.5))
        bpy.ops.transform.rotate(value=-0.523599, orient_axis='Y')

        bpy.ops.mesh.primitive_cylinder_add()
        bpy.ops.transform.translate(value=(0.7,0,-3.5))
        bpy.ops.transform.resize(value=(0.5,0.5,2))
        #bpy.ops.transform.rotate(value=0.323599, orient_axis='Y')

        bpy.ops.mesh.primitive_cylinder_add()
        bpy.ops.transform.translate(value=(-0.7,0,-3.5))
        bpy.ops.transform.resize(value=(0.5,0.5,2))
        #bpy.ops.transform.rotate(value=-0.323599, orient_axis='Y')

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        print("Monkey spawned center scene!")
        try:
            self.spawn()
        except Exception as e:
            print(e)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(PANEL_PT_TestPanel)
    bpy.utils.register_class(MindsOperator)
    bpy.utils.register_class(MonkeyOperator)
    
def unregister():
    bpy.utils.unregister_class(PANEL_PT_TestPanel)
    bpy.utils.unregister_class(MindsOperator)
    bpy.utils.unregister_class(MonkeyOperator)
    
if __name__ == "__main__":
    register()
    # test call - same thing happens when you push the button in the panel
    
    #    bpy.ops.object.minds_operator()
    bpy.ops.object.monkey_operator()