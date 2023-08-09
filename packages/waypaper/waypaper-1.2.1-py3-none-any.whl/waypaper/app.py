"""Module that runs GUI app"""

import gi
import os
import subprocess
import configparser

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf, Gdk

from waypaper.changer import change_wallpaper
from waypaper.config import cf


def get_image_paths(root_folder, include_subfolders=False, depth=None):
    """Get a list of file paths depending of weather we include subfolders and how deep we scan"""
    file_paths = []
    for root, directories, files in os.walk(root_folder):
        if not include_subfolders and root != root_folder:
            continue
        if depth is not None and root != root_folder:
            current_depth = root.count(os.path.sep) - root_folder.count(os.path.sep)
            if current_depth > depth:
                continue
        for filename in files:
            if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".gif"):
                file_paths.append(os.path.join(root, filename))
    return file_paths


class App(Gtk.Window):
    """Main application class that controls GUI"""

    def __init__(self):
        super().__init__(title="Waypaper")
        self.set_default_size(780, 600)

        # Create a vertical box for layout:
        self.main_box = Gtk.VBox(spacing=10)
        self.add(self.main_box)

        # Create a button to open folder dialog:
        self.choose_folder_button = Gtk.Button(label="Choose wallpaper folder")
        self.choose_folder_button.connect("clicked", self.on_choose_folder_clicked)
        self.main_box.pack_start(self.choose_folder_button, False, False, 0)

        # Create an alignment container to place the grid in the top-right corner:
        self.grid_alignment = Gtk.Alignment(xalign=1, yalign=0.0, xscale=0.5, yscale=1)
        self.main_box.pack_start(self.grid_alignment, True, True, 0)

        # Create a scrolled window for the grid:
        self.scrolled_window = Gtk.ScrolledWindow()
        self.scrolled_window.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.grid_alignment.add(self.scrolled_window)

        # Create a grid layout for images:
        self.grid = Gtk.Grid()
        self.grid.set_row_spacing(0)
        self.grid.set_column_spacing(0)
        self.scrolled_window.add(self.grid)

        # Create subfolder toggle:
        self.include_subfolders_checkbox = Gtk.ToggleButton(label="Subfolders")
        self.include_subfolders_checkbox.set_active(cf.include_subfolders)
        self.include_subfolders_checkbox.connect("toggled", self.on_include_subfolders_toggled)

        # Create a fill option dropdown menu:
        # self.fill_option_label = Gtk.Label(label="")
        self.fill_option_combo = Gtk.ComboBoxText()
        self.fill_option_combo.append_text("Fill")
        self.fill_option_combo.append_text("Stretch")
        self.fill_option_combo.append_text("Fit")
        self.fill_option_combo.append_text("Center")
        self.fill_option_combo.append_text("Tile")
        self.fill_option_combo.set_active(0)
        self.fill_option_combo.connect("changed", self.on_fill_option_changed)

        # Create exit button:
        self.exit_button = Gtk.Button(label=" Exit ")
        self.exit_button.connect("clicked", self.on_exit_clicked)

        # Create a box to contain the bottom row of buttons with margin
        self.bottom_button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=20)
        self.bottom_button_box.set_margin_bottom(10)
        self.main_box.pack_end(self.bottom_button_box, False, False, 0)

        # Create an alignment container to center align the row of buttons
        self.button_row_alignment = Gtk.Alignment(xalign=0.5, yalign=0.0, xscale=0.5, yscale=0.5)
        self.bottom_button_box.pack_start(self.button_row_alignment, True, False, 0)

        # Create a horizontal box for display option and exit button
        self.options_box = Gtk.HBox(spacing=10)
        self.options_box.pack_start(self.include_subfolders_checkbox, False, False, 0)
        # self.options_box.pack_start(self.fill_option_label, False, False, 0)
        self.options_box.pack_start(self.fill_option_combo, False, False, 0)
        self.options_box.pack_end(self.exit_button, False, False, 0)
        self.button_row_alignment.add(self.options_box)

        # Connect the "q" key press event to exit the application
        self.connect("key-press-event", self.on_key_pressed)


    def load_images(self):
        """Load images from the selected folder, resize them, and arrange int grid"""

        # Clear existing images:
        for child in self.grid.get_children():
            self.grid.remove(child)

        row = 0
        col = 0

        # Load images from the folder:
        image_paths = get_image_paths(cf.image_folder, cf.include_subfolders, depth=1)
        for image_path in image_paths:

            # Load and scale the image:
            pixbuf = GdkPixbuf.Pixbuf.new_from_file(image_path)
            aspect_ratio = pixbuf.get_width() / pixbuf.get_height()
            scaled_width = 240
            scaled_height = int(scaled_width / aspect_ratio)
            scaled_pixbuf = pixbuf.scale_simple(scaled_width, scaled_height, GdkPixbuf.InterpType.BILINEAR)

            # Create a button with an image inside:
            image = Gtk.Image.new_from_pixbuf(scaled_pixbuf)
            button = Gtk.Button()
            button.set_relief(Gtk.ReliefStyle.NONE)  # Remove border
            button.add(image)

            # Add button to the grid and connect clicked event:
            self.grid.attach(button, col, row, 1, 1)
            button.connect("clicked", self.on_image_clicked, image_path)

            col += 1
            if col >= 3:
                col = 0
                row += 1

        # Show all images:
        self.grid.show_all()


    def on_choose_folder_clicked(self, widget):
        """Choosing the folder of images, saving the path, and reloading images"""

        dialog = Gtk.FileChooserDialog(
            "Please choose a folder", self, Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Select", Gtk.ResponseType.OK)
        )
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            cf.image_folder = dialog.get_filename()
            cf.save()
            self.load_images()
        dialog.destroy()


    def on_include_subfolders_toggled(self, toggle):
        """On chosing to include subfolders"""
        cf.include_subfolders = toggle.get_active()
        self.load_images()


    def on_fill_option_changed(self, combo):
        cf.fill_option = combo.get_active_text()


    def on_image_clicked(self, widget, user_data):
        """On clicking an image, set it as a wallpaper and save"""
        cf.wallpaper = user_data
        print("Selected image path:", cf.wallpaper)
        cf.fill_option = self.fill_option_combo.get_active_text() or cf.fill_option
        change_wallpaper(cf.wallpaper, cf.fill_option)
        cf.save()


    def on_exit_clicked(self, widget):
        """On clicking exit button, save the data and quit"""
        cf.save()
        Gtk.main_quit()


    def on_key_pressed(self, widget, event):
        """On clicking q, save the data and quit"""
        if event.keyval == Gdk.KEY_q:
            cf.save()
            Gtk.main_quit()


    def run(self):
        """Run GUI application"""
        self.load_images()
        self.connect("destroy", self.on_exit_clicked)
        self.show_all()
        Gtk.main()
