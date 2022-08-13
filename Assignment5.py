import tkinter as T  # Renamed package "T"
import tkinter.messagebox as TKM  # rename as "TKM"


class MPGCalculator:
    def __init__(self, miles, gallons):
        if miles >= 0:
            self.miles = miles
            if gallons > 0:
                self.gallons = gallons

                self.MPG_window = T.Tk()
                self.titlelabel = T.Label(self.MPG_window, text="Miles Per Gallon Calculator")
                self.titlelabel.pack(side="top")
                self.mileLabel = T.Label(self.MPG_window, text="Enter Miles:")
                self.mileLabel.pack(side="left")
                self.EtrMiles = T.Entry(width=10)
                self.EtrMiles.pack(side="left")
                self.gallonLabel = T.Label(self.MPG_window, text="Enter Gallons:")
                self.gallonLabel.pack(side="left")
                self.EtrGallons = T.Entry(width=10)
                self.EtrGallons.pack(side="left")
                self.MPG_button = T.Button(text="Calculate MPG", command=self.Calculate)
                self.MPG_button.pack(side="top")
                self.MPG_button = T.Button(text="CANCEL", command=self.MPG_window.destroy)
                self.MPG_button.pack(side="bottom")

                T.mainloop()
            else:
                print("Value of gallons not valid! Must be > 0.")
        else:
            print("Value of miles not valid! Must be >= 0.")

    def set_miles(self, miles):
        if miles >= 0:
            self.miles = miles
        else:
            print("Value of miles not valid! Must be >= 0.")

    def get_miles(self):
        return self.miles

    def set_gallons(self, gallons):
        if gallons > 0:
            self.gallons = gallons
        else:
            print("Value of gallons not valid! Must be > 0.")

    def get_gallons(self):
        return self.gallons

    def Calculate(self):
        YourMiles = float(self.EtrMiles.get())
        YourGallons = float(self.EtrGallons.get())
        if YourMiles >= 0:
            if YourGallons > 0:
                self.set_miles(YourMiles)
                self.set_gallons(YourGallons)
                MPG = self.get_miles() / self.get_gallons()
                TKM.showinfo("Your car's mileage is...", str(MPG) + "\nmiles per gallon.")
            else:
                TKM.showinfo("ERROR!", "Value of gallons not valid! Must be > 0.")
        else:
            TKM.showinfo("ERROR!", "Value of miles not valid! Must be >= 0.")


GUI = MPGCalculator(5, 5)
