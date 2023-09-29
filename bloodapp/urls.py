from django.urls import path
from bloodapp import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('', views.adminlogin, name="adminlogin"),
    path('adminloginfun/', views.adminloginfun, name="adminloginfun"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),

    path('hospital/', views.hospital, name="hospital"),
    path('savehospital/',views.savehospital, name="savehospital"),
    path('hospitaldisplay/',views.hospitaldisplay, name="hospitaldisplay"),
    path('hospitaldelete/<int:dataid>/',views.hospitaldelete, name="hospitaldelete"),

    path('bloodadd/', views.addblood, name="addblood"),
    path('saveblood/', views.saveblood, name="saveblood"),
    path('blooddisplay/', views.blooddisplay, name="blooddisplay"),
    path('bloodedit/<int:dataid>/', views.bloodedit, name="bloodedit"),
    path('bloodupdate/<int:dataid>/', views.bloodupdate, name="bloodupdate"),
    path('blooddelete/<int:dataid>/', views.blooddelete, name="blooddelete"),

    path('requesthisory/', views.requesthisory, name="requesthisory"),
    path('saverequest/', views.saverequest, name="saverequest"),

    path('displaydonate1/', views.displaydonate, name="donatedonate"),
    path('displayrequest/', views.displayrequest, name="displayrequest"),
    path('displaysupport/', views.displaysupport, name="displaysupport"),
    path('displayregister/', views.displayregister, name="displayregister"),

    path('adminactivity/', views.adminactivity, name="adminactivity"),
    path('useractivity/', views.useractivity, name="useractivity"),

    path('deleteregister/<int:dataid>/', views.deleteregister, name="deleteregister"),
    path('deleterequest/<int:dataid>/', views.deleterequest, name="deleterequest"),
    path('deleteoldrequest/<int:dataid>/', views.deleteoldrequest, name="deleteoldrequest"),

    path('faqnotes/', views.faqnotes, name="faqnotes"),
    path('savefaq/', views.savefaq, name="savefaq"),
    path('displayfaq/', views.displayfaq, name="displayfaq"),

    path('article/', views.article, name="article"),
    path('savearticle/', views.savearticle, name="savearticle"),
    path('displayarticles/', views.displayarticles, name="displayarticles"),
    path('deletearticle/<int:dataid>/', views.deletearticle, name="deletearticle"),


]
