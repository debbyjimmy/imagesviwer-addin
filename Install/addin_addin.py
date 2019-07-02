import pythonaddins
import os
import functools
import threading
import webbrowser

class n1(object):
    """Implementation for addin_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Composite Shapefiles/Erosion_Site.kmz")   
        pythonaddins.MessageBox("The points are now opened on google earth. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n10(object):
    """Implementation for addin_addin.button_9 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Soil Maps/Other Maps/NEWMAP_AK_Composite_soil_text_1.pdf")   
        pythonaddins.MessageBox("The map is opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n12(object):
    """Implementation for addin_addin.button_10 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Soil Maps/Other Maps/NEWMAP_AK_Composite_NDVI_1.pdf")   
        pythonaddins.MessageBox("The map is opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n13(object):
    """Implementation for addin_addin.button_11 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Other Maps/NEWMAP_AK_Composite_Slope_1.pdf")   
        pythonaddins.MessageBox("The map is opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n14(object):
    """Implementation for addin_addin.button_12 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Other Maps/NEWMAP_AK_Composite_P_factor_1.pdf")   
        pythonaddins.MessageBox("The map is opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n15(object):
    """Implementation for addin_addin.button_13 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Other Maps/NEWMAP_AK_Composite_C_factor_1.pdf")   
        pythonaddins.MessageBox("The map is opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n16(object):
    """Implementation for addin_addin.button_14 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Other Maps/NEWMAP_AK_Composite_DEM_1.pdf")   
        pythonaddins.MessageBox("The map is opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n17(object):
    """Implementation for addin_addin.button_15 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Other Maps/NEWMAP_AK_Composite_flow_acc_1.pdf")   
        pythonaddins.MessageBox("The map is opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n18(object):
    """Implementation for addin_addin.button_16 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Other maps/NEWMAP_AK_Composite_flow_dir_1.pdf")   
        pythonaddins.MessageBox("The map is opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n19(object):
    """Implementation for addin_addin.button_17 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Other Maps/NEWMAP_AK_Composite_admin_1.pdf")   
        pythonaddins.MessageBox("The map is opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n2(object):
    """Implementation for addin_addin.button_1 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Other Maps/NEWMAP_AK_Composite_Geological_1.pdf")   
        pythonaddins.MessageBox("The map is opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n20(object):
    """Implementation for addin_addin.button_18 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Other Maps/NEWMAP_AK_Composite_Drainage_1.pdf")   
        pythonaddins.MessageBox("The map is opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n21(object):
    """Implementation for addin_addin.button_19 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Other Maps/NEWMAP_AK_Composite_Drainage_density_1.pdf")   
        pythonaddins.MessageBox("The map is opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n22(object):
    """Implementation for addin_addin.button_20 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Other Maps/NEWMAP_AK_Composite_erosion_1.pdf")   
        pythonaddins.MessageBox("The map is opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n23(object):
    """Implementation for addin_addin.button_21 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Other Maps/NEWMAP_AK_Composite_flood_1.pdf")   
        pythonaddins.MessageBox("The map is opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n24(object):
    """Implementation for addin_addin.button_22 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Other Maps/NEWMAP_AK_Composite_land_cover_1.pdf")   
        pythonaddins.MessageBox("The map is opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n25(object):
    """Implementation for addin_addin.button_23 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Other Maps/NEWMAP_AK_Composite_population_1.pdf")   
        pythonaddins.MessageBox("The map is opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n26(object):
    """Implementation for addin_addin.button_24 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Other Maps/NEWMAP_AK_Composite_Rainfall_1.pdf")   
        pythonaddins.MessageBox("The map is opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n27(object):
    """Implementation for addin_addin.button_25 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Other Maps/NEWMAP_AK_Composite_watershed.pdf")   
        pythonaddins.MessageBox("The map is opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n3(object):
    """Implementation for addin_addin.button_2 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Topo Sheets/NEWMAP_AK_Topo-1.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Topo Sheets/NEWMAP_AK_Topo-2.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Topo Sheets/NEWMAP_AK_Topo-3.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Topo Sheets/NEWMAP_AK_Topo-4.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Topo Sheets/NEWMAP_AK_Topo-5.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Topo Sheets/NEWMAP_AK_Topo-6.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Topo Sheets/NEWMAP_AK_Topo-7.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Topo Sheets/NEWMAP_AK_Topo-8.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Topo Sheets/NEWMAP_AK_Topo-9.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Topo Sheets/NEWMAP_AK_Topo-10.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Topo Sheets/NEWMAP_AK_Topo-11.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Topo Sheets/NEWMAP_AK_Topo-12.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Topo Sheets/NEWMAP_AK_Topo-13.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Topo Sheets/NEWMAP_AK_Topo-14.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Topo Sheets/NEWMAP_AK_Topo-15.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Topo Sheets/NEWMAP_AK_Topo-16.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Topo Sheets/NEWMAP_AK_Topo-17.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Topo Sheets/NEWMAP_AK_Topo-18.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Topo Sheets/NEWMAP_AK_Topo-19.pdf")
        pythonaddins.MessageBox("The maps are in sheet 1-19 and opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n5(object):
    """Implementation for addin_addin.button_4 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Erosion Risk Maps/NEWMAP_AK_RUSLE-01.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Erosion Risk Maps/NEWMAP_AK_RUSLE-02.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Erosion Risk Maps/NEWMAP_AK_RUSLE-03.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Erosion Risk Maps/NEWMAP_AK_RUSLE-04.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Erosion Risk Maps/NEWMAP_AK_RUSLE-05.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Erosion Risk Maps/NEWMAP_AK_RUSLE-06.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Erosion Risk Maps/NEWMAP_AK_RUSLE-07.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Erosion Risk Maps/NEWMAP_AK_RUSLE-08.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Erosion Risk Maps/NEWMAP_AK_RUSLE-09.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Erosion Risk Maps/NEWMAP_AK_RUSLE-10.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Erosion Risk Maps/NEWMAP_AK_RUSLE-11.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Erosion Risk Maps/NEWMAP_AK_RUSLE-12.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Erosion Risk Maps/NEWMAP_AK_RUSLE-13.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Erosion Risk Maps/NEWMAP_AK_RUSLE-14.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Erosion Risk Maps/NEWMAP_AK_RUSLE-15.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Erosion Risk Maps/NEWMAP_AK_RUSLE-16.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Erosion Risk Maps/NEWMAP_AK_RUSLE-17.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Erosion Risk Maps/NEWMAP_AK_RUSLE-18.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Erosion Risk Maps/NEWMAP_AK_RUSLE-19.pdf")
        pythonaddins.MessageBox("The maps are in sheet 1-19 and opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n6(object):
    """Implementation for addin_addin.button_5 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Watershed Maps/NEWMAP_AK_Watershed-01.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Watershed Maps/NEWMAP_AK_Watershed-02.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Watershed Maps/NEWMAP_AK_Watershed-03.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Watershed Maps/NEWMAP_AK_Watershed-04.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Watershed Maps/NEWMAP_AK_Watershed-05.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Watershed Maps/NEWMAP_AK_Watershed-06.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Watershed Maps/NEWMAP_AK_Watershed-07.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Watershed Maps/NEWMAP_AK_Watershed-08.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Watershed Maps/NEWMAP_AK_Watershed-09.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Watershed Maps/NEWMAP_AK_Watershed-10.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Watershed Maps/NEWMAP_AK_Watershed-11.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Watershed Maps/NEWMAP_AK_Watershed-12.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Watershed Maps/NEWMAP_AK_Watershed-13.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Watershed Maps/NEWMAP_AK_Watershed-14.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Watershed Maps/NEWMAP_AK_Watershed-15.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Watershed Maps/NEWMAP_AK_Watershed-16.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Watershed Maps/NEWMAP_AK_Watershed-17.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Watershed Maps//NEWMAP_AK_Watershed-18.pdf")
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Watershed Maps//NEWMAP_AK_Watershed-19.pdf")
        pythonaddins.MessageBox("The maps are in sheet 1-19 and opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n7(object):
    """Implementation for addin_addin.button_6 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Other Maps/NEWMAP_AK_Composite_Soill_1.pdf")   
        pythonaddins.MessageBox("The map is opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n8(object):
    """Implementation for addin_addin.button_7 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Other Maps/NEWMAP_AK_Composite_soil_ph_1.pdf")   
        pythonaddins.MessageBox("The map is opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n9(object):
    """Implementation for addin_addin.button_8 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Other Maps/NEWMAP_AK_Composite_soil_suitability_1.pdf")   
        pythonaddins.MessageBox("The map is opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n28(object):
    """Implementation for addin_addin.button_26 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Other Maps/NEWMAP_AK_Composite_Soil_erodibility_1.pdf")   
        pythonaddins.MessageBox("The map is opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n29(object):
    """Implementation for addin_addin.button_27 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Other Maps/NEWMAP_AK_Composite_Slope_length_1.pdf")   
        pythonaddins.MessageBox("The map is opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n30(object):
    """Implementation for addin_addin.button_28 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Other Maps/NEWMAP_AK_Composite_R_factor_1.pdf")   
        pythonaddins.MessageBox("The map is opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

class n31(object):
    """Implementation for addin_addin.button_29 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        def run_in_other_thread(function): #conflicts w/ os.startfile will crash arcmap.  this is a workaround
         # functool.wraps will copy over the docstring and some other metadata
         # from the original function
         @functools.wraps(function)
         def fn_(*args, **kwargs):
          thread = threading.Thread(target=function, args=args, kwargs=kwargs)
          thread.start()
          thread.join()
         return fn_
        startfile = run_in_other_thread(os.startfile)
        startfile("C:/NEWMAP EROSION PROJECT-AKW/Composite Site Data/Maps/Other Maps/NEWMAP_AK_Composite_E_Site.pdf")   
        pythonaddins.MessageBox("The map is opened. Simply minimize Arcmap and view it well.",0)
        arcpy.RefreshActiveView()

