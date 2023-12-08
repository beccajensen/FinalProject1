import csv
import time

class Logic:
    """
    Class representing the logic for a simple GUI controller.
    """

    def __init__(self, gui):
        """
        Initialize the Logic object.

        Parameters:
        - gui: The GUI object associated with this logic.
        """
        self.gui = gui
        self.mute = False
        self.channel = 0
        self.volume = 0
        self.csv_file = None  # CSV file object

        # Connect GUI signals to corresponding methods
        self.gui.chan_up.clicked.connect(self.increment_channel)
        self.gui.chan_down.clicked.connect(self.decrement_channel)
        self.gui.vol_up.clicked.connect(self.increment_volume)
        self.gui.vol_down.clicked.connect(self.decrement_volume)
        self.gui.MUTE.clicked.connect(self.mute_volume)
        self.gui.power.clicked.connect(self.toggle_power)
        self.toggle_power()

    def toggle_power(self):
        """
        Toggle the power state and update the GUI controls accordingly.

        Returns:
        None
        """
        if self.gui.power.text() == "OFF":
            # Turn off
            self.gui.vol_num.display(0)
            self.gui.power.setText("ON")
            self.disable_controls(True)  # Disable controls
            self.gui.chan_num.display(0)

            # Close the existing CSV file if it's open
            if self.csv_file:
                self.csv_file.close()
        else:
            # Turn on
            self.gui.power.setText("OFF")
            self.disable_controls(False)  # Enable controls
            self.gui.chan_num.display(self.channel)
            self.gui.vol_num.display(self.volume)

            # Open a new CSV file for writing in append mode
            self.csv_file = open("power_data.csv", mode="a", newline="")
            csv_writer = csv.writer(self.csv_file)

            # Check if the file is empty and write header if needed
            if self.csv_file.tell() == 0:
                csv_writer.writerow(["Time", "Channel", "Volume"])



    def increment_channel(self):
        """
        Increment the channel by 1 if it's less than 3.

        Returns:
        None
        """
        if self.channel < 3:
            self.channel += 1
            self.gui.chan_num.display(self.channel)
            self.write_to_csv()

    def decrement_channel(self):
        """
        Decrement the channel by 1 if it's greater than 0.

        Returns:
        None
        """
        if self.channel > 0:
            self.channel -= 1
            self.gui.chan_num.display(self.channel)
            self.write_to_csv()

    def increment_volume(self):
        """
        Increment the volume by 1 if it's less than 3.

        Returns:
        None
        """
        if self.volume < 3:
            self.volume += 1
            self.gui.vol_num.display(self.volume)
            self.write_to_csv()

    def decrement_volume(self):
        """
        Decrement the volume by 1 if it's greater than 0.

        Returns:
        None
        """
        if self.volume > 0:
            self.volume -= 1
            self.gui.vol_num.display(self.volume)
            self.write_to_csv()

    def mute_volume(self):
        """
        Toggle the mute state and update the GUI display accordingly.

        Returns:
        None
        """
        self.mute = not self.mute
        if self.mute:
            self.gui.vol_num.display(0)
        else:
            self.gui.vol_num.display(self.volume)
        self.write_to_csv()

    def write_to_csv(self):
        """
        Write current data to the CSV file.

        Returns:
        None
        """
        if self.csv_file:
            csv_writer = csv.writer(self.csv_file)
            csv_writer.writerow([time.time(), self.channel, self.volume])

    def disable_controls(self, disable: bool):
        """
        Enable or disable GUI controls.

        Parameters:
        - disable: A boolean indicating whether to disable or enable the controls.

        Returns:
        None
        """
        self.gui.vol_up.setDisabled(disable)
        self.gui.vol_down.setDisabled(disable)
        self.gui.chan_up.setDisabled(disable)
        self.gui.chan_down.setDisabled(disable)
        self.gui.MUTE.setDisabled(disable)
