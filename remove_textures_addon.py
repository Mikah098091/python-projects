bl_info = {
    "name": "Remove Image Textures",
    "author": "MikahHD",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Object > Remove Image Textures",
    "description": "Remove all image texture nodes from selected objects",
    "category": "Object",
}

import bpy

class OBJECT_OT_remove_image_textures(bpy.types.Operator):
    """Remove all Image Texture nodes from selected objects"""
    bl_idname = "object.remove_image_textures"
    bl_label = "Remove Image Textures"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        removed_count = 0
        selected_objects = context.selected_objects
        
        if not selected_objects:
            self.report({'WARNING'}, "No objects selected!")
            return {'CANCELLED'}
        
        # Get materials from selected objects
        materials_to_process = set()
        for obj in selected_objects:
            if hasattr(obj.data, 'materials'):
                for mat in obj.data.materials:
                    if mat:
                        materials_to_process.add(mat)
        
        # Remove Image Texture nodes from those materials
        for material in materials_to_process:
            if material.use_nodes:
                nodes_to_remove = []
                
                for node in material.node_tree.nodes:
                    if node.type == 'TEX_IMAGE':
                        nodes_to_remove.append(node)
                
                for node in nodes_to_remove:
                    material.node_tree.nodes.remove(node)
                    removed_count += 1
        
        # Remove unused images
        removed_images = 0
        for image in list(bpy.data.images):
            if image.users == 0:
                bpy.data.images.remove(image)
                removed_images += 1
        
        self.report({'INFO'}, f"Removed {removed_count} texture nodes and {removed_images} unused images")
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(OBJECT_OT_remove_image_textures.bl_idname)


def register():
    bpy.utils.register_class(OBJECT_OT_remove_image_textures)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_remove_image_textures)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()
