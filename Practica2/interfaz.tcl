#############################################################################
# Generated by PAGE version 6.1
#  in conjunction with Tcl version 8.6
#  Apr 27, 2021 03:27:21 AM CDT  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top45 {base} {
    global vTcl
    if {$base == ""} {
        set base .top45
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m51" -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 600x450+369+155
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 2394 749
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "DES Cipher"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    text $top.tex46 \
        -background white -font TkTextFont -foreground black \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -inactiveselectbackground #000000 -insertbackground black \
        -selectbackground blue -selectforeground white -width 204 -wrap word 
    $top.tex46 configure -font "TkTextFont"
    $top.tex46 insert end text
    vTcl:DefineAlias "$top.tex46" "txtKey" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab48 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Key: 
    vTcl:DefineAlias "$top.lab48" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab49 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Method: 
    vTcl:DefineAlias "$top.lab49" "Method" vTcl:WidgetProc "Toplevel1" 1
    menu $top.m51 \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background $vTcl(actual_gui_menu_bg) \
        -font TkMenuFont -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    ttk::combobox $top.tCo52 \
        -textvariable combobox -foreground {} -background {} -takefocus {} 
    vTcl:DefineAlias "$top.tCo52" "TCombobox1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but54 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Decrypt 
    vTcl:DefineAlias "$top.but54" "btnDecrypt" vTcl:WidgetProc "Toplevel1" 1
    button $top.but55 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Encrypt 
    vTcl:DefineAlias "$top.but55" "btnEncrypt" vTcl:WidgetProc "Toplevel1" 1
    text $top.tex56 \
        -background white -font TkTextFont -foreground black -height 264 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 464 -wrap word 
    $top.tex56 configure -font "TkTextFont"
    $top.tex56 insert end text
    vTcl:DefineAlias "$top.tex56" "intImg" vTcl:WidgetProc "Toplevel1" 1
    button $top.but57 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Open File} 
    vTcl:DefineAlias "$top.but57" "btnFile" vTcl:WidgetProc "Toplevel1" 1
    text $top.tex45 \
        -background white -font TkTextFont -foreground black -height 24 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 74 -wrap word 
    $top.tex45 configure -font "TkTextFont"
    $top.tex45 insert end text
    vTcl:DefineAlias "$top.tex45" "Text1" vTcl:WidgetProc "Toplevel1" 1
    ttk::label $top.tLa46 \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -relief flat -anchor w -justify left -text C0: 
    vTcl:DefineAlias "$top.tLa46" "tbl" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $top.che48 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text {C0 random} -variable che48 
    vTcl:DefineAlias "$top.che48" "Checkbutton1" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tex46 \
        -in $top -x 0 -relx 0.2 -y 0 -rely 0.133 -width 0 -relwidth 0.34 \
        -height 0 -relheight 0.053 -anchor nw -bordermode ignore 
    place $top.lab48 \
        -in $top -x 0 -relx 0.133 -y 0 -rely 0.133 -width 0 -relwidth 0.057 \
        -height 0 -relheight 0.047 -anchor nw -bordermode ignore 
    place $top.lab49 \
        -in $top -x 0 -relx 0.1 -y 0 -rely 0.2 -width 0 -relwidth 0.09 \
        -height 0 -relheight 0.047 -anchor nw -bordermode ignore 
    place $top.tCo52 \
        -in $top -x 0 -relx 0.2 -y 0 -rely 0.2 -width 0 -relwidth 0.238 \
        -height 0 -relheight 0.047 -anchor nw -bordermode ignore 
    place $top.but54 \
        -in $top -x 0 -relx 0.817 -y 0 -rely 0.289 -width 47 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but55 \
        -in $top -x 0 -relx 0.717 -y 0 -rely 0.289 -width 47 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $top.tex56 \
        -in $top -x 0 -relx 0.15 -y 0 -rely 0.356 -width 0 -relwidth 0.773 \
        -height 0 -relheight 0.587 -anchor nw -bordermode ignore 
    place $top.but57 \
        -in $top -x 0 -relx 0.15 -y 0 -rely 0.289 -width 77 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $top.tex45 \
        -in $top -x 0 -relx 0.683 -y 0 -rely 0.133 -width 0 -relwidth 0.123 \
        -height 0 -relheight 0.053 -anchor nw -bordermode ignore 
    place $top.tLa46 \
        -in $top -x 0 -relx 0.633 -y 0 -rely 0.133 -width 0 -relwidth 0.042 \
        -height 0 -relheight 0.042 -anchor nw -bordermode ignore 
    place $top.che48 \
        -in $top -x 0 -relx 0.633 -y 0 -rely 0.2 -width 0 -relwidth 0.135 \
        -height 0 -relheight 0.056 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}



set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top45 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

