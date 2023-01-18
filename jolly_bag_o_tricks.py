#bl_info = {
#    "name": "Object Adder",
#    "author": "TheJollyLaMa",
#    "version": (1,0),
#    "blender": (3.3.0,0),
#    "location": "View3d > Tool",
#    "warning": "",
#    "wiki_url": "",
#    "category": "Add Mesh"
#}

import bpy
import requests
import json

class PANEL_PT_TestPanel(bpy.types.Panel):
    bl_label = "J Block (WEB3)"
    bl_idname = "PANEL_PT_TestPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Jolly\'s Bag \'O Tricks'
    
    def draw(self, context):
        layout = self.layout
        
#        # add a cube
#        rowA = layout.row()
#        rowA.label(text="Add a cube", icon="CUBE")
#        rowA.operator("mesh.primitive_cube_add")
#        
#        # add a uv sphere
#        rowB = layout.row()
#        rowB.label(text="Add a uv sphere", icon="SPHERE")
#        rowB.operator("mesh.primitive_uv_sphere_add")
#        
#        #add a text object
#        rowC = layout.row()
#        rowC.label(text="Add an object", icon="OUTLINER_OB_FONT")
#        rowC.operator("object.text_add")

#        #add a bunch of objects
#        rowC = layout.row()
#        rowC.label(text="Add a group", icon="SOLO_OFF")
#        #for i in range(20):
#        rowC.operator("mesh.primitive_uv_sphere_add")

        # pin to local ipfs node
        row1 = layout.row()
        row1.label(text="IPFS", icon='META_CUBE')
        row1.operator(IpfsOperator.bl_idname, text=IpfsOperator.bl_label)

        # post to Minds
        row2 = layout.row()
        row2.label(text="MINDS", icon="OUTLINER_DATA_LIGHT")
        row2.operator(MindsOperator.bl_idname, text=MindsOperator.bl_label)

        # saves creative session to Infinite Imaginarium
        row3 = layout.row()
        row3.label(text="Infinite Imaginarium", icon="FORCE_VORTEX")
        row3.operator(InfImgOperator.bl_idname, text=InfImgOperator.bl_label)        
        
        # Mint on OpenSea
        row4 = layout.row()
        row4.label(text="OPEN SEA", icon="OUTLINER_OB_FORCE_FIELD")
        row4.operator(OpenSeaOperator.bl_idname, text=OpenSeaOperator.bl_label)

        # GarageBand funhouse connections
        row4 = layout.row()
        row4.label(text="GarageBand", icon="SPEAKER")
        row4.operator(GarageBandOperator.bl_idname, text=GarageBandOperator.bl_label)

        # WhiteBoard connections
        row4 = layout.row()
        row4.label(text="WhiteBoards", icon="WORLD_DATA")
        row4.operator(WhiteBoardOperator.bl_idname, text=WhiteBoardOperator.bl_label)

        # send in email
        row5 = layout.row()
        row5.label(text="EMAIL", icon="EXPORT")

        # Spawn monkey
        row6 = layout.row()
        row6.label(text="MONKEY", icon="MONKEY")
        row6.operator(MonkeyOperator.bl_idname, text=MonkeyOperator.bl_label)
    
class IpfsOperator(bpy.types.Operator):
    """Pin file to local IPFS node"""
    bl_idname = "object.ipfs_operator"
    bl_label = "Pin to IPFS"
    local_ipfs_path = "http://localhost:5001"
    def add(self):
        
        files = {
            'file1': open('/Users/J/Desktop/toon_head.png', 'rb')
        }

        try:
            response = requests.post(self.local_ipfs_path + '/api/v0/add', files=files)
            hash = json.loads(response.text)['Hash']
            print("IPFS CID Hash: {}".format(hash))
            return hash
        except Exception as e:
            print(e)
            
    def pin(self, hash):
        print(hash)
        try:
            r = requests.post(ipfs_path = self.local_ipfs_path + '/api/v0/pin/add' + hash )
            print(r.text)
        except Exception as e:
            print(e)
            
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        print("Follow the White Rabbit to the InterPlanetary FileSystem")
        try:
            self.pin(self.add())
            
        except Exception as e:
            print(e)

        return {'FINISHED'}

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

class InfImgOperator(bpy.types.Operator):
    """Send creation to Infinite Imaginarium Server"""
    bl_idname = "object.infimg_operator"
    bl_label = "Save to Server"    
    def post(self):
        pass
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        print("Follow the White Rabbit to the Infinite Imaginarium")
        try:
            self.post()
        except Exception as e:
            print(e)
            
        return {'FINISHED'}
    
class OpenSeaOperator(bpy.types.Operator):
    """Mint creation on OpenSea"""
    bl_idname = "object.opensea_operator"
    bl_label = "Mint on OpenSea"    
    def mint(self):
        pass
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        print("Follow the White Rabbit to OpenSea")
        try:
            self.mint()
        except Exception as e:
            print(e)
        return {'FINISHED'}

class GarageBandOperator(bpy.types.Operator):
    """Connects to GarageBand functionality """
    bl_idname = "object.garageband_operator"
    bl_label = "GarageBand Live"    
    def add_mic_channel(self):
        """add a mic channel from garageband"""
        pass
    def add_instrument(self):
        """add an instrument channel from garageband"""    
        pass
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        print("Follow the White Rabbit into and back out of GarageBand Live Visualizer")
        try:
            self.add_mic_channel()
            self.add_instrument()
        except Exception as e:
            print(e)
        return {'FINISHED'}

class WhiteBoardOperator(bpy.types.Operator):
    """Connects to various whiteboards for collaborations"""
    bl_idname = "object.whiteboard_operator"
    bl_label = "Send to WhiteBoard"    
    def lucid_export(self):
        """export to a lucid chart"""
        print("Export to LucidChart")
        pass
    def miro_export(self):
        """export to a miro board"""    
        print("Export to MiroBoard")    
        pass
    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        print("Follow the White Rabbit into a lucid chart, miro board, or figma jam, etc.")
        try:
            self.lucid_export()
            self.miro_export()
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
    bpy.utils.register_class(IpfsOperator)
    bpy.utils.register_class(MindsOperator)
    bpy.utils.register_class(InfImgOperator)
    bpy.utils.register_class(OpenSeaOperator)
    bpy.utils.register_class(GarageBandOperator)
    bpy.utils.register_class(WhiteBoardOperator)
    bpy.utils.register_class(MonkeyOperator)
    
def unregister():
    bpy.utils.unregister_class(PANEL_PT_TestPanel)
    bpy.utils.unregister_class(IpfsOperator)
    bpy.utils.unregister_class(MindsOperator)
    bpy.utils.unregister_class(InfImgOperator)
    bpy.utils.unregister_class(OpenSeaOperator)
    bpy.utils.unregister_class(GarageBandOperator)
    bpy.utils.unregister_class(WhiteBoardOperator)
    bpy.utils.unregister_class(MonkeyOperator)
    
if __name__ == "__main__":
    register()
    # test call - same thing happens when you push the button in the panel

#    bpy.ops.object.ipfs_operator()
#    bpy.ops.object.minds_operator()
#    bpy.ops.object.infimg_operator()
#    bpy.ops.object.opensea_operator()
#    bpy.ops.object.garageband_operator()
#    bpy.ops.object.whiteboard_operator()
    bpy.ops.object.monkey_operator()