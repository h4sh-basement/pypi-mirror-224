/*****************************************************************************\
* (c) Copyright 2019 CERN for the benefit of the LHCb Collaboration           *
*                                                                             *
* This software is distributed under the terms of the GNU General Public      *
* Licence version 3 (GPL Version 3), copied verbatim in the file "LICENSE".   *
*                                                                             *
* In applying this licence, CERN does not waive the privileges and immunities *
* granted to it by virtue of its status as an Intergovernmental Organization  *
* or submit itself to any jurisdiction.                                       *
\*****************************************************************************/
Ext.define("LHCbDIRAC.RAWIntegrityMonitor.classes.RAWIntegrityMonitor", {
  extend: "Ext.dirac.core.Module",

  requires: [
    "Ext.util.*",
    "Ext.panel.Panel",
    "Ext.form.field.Text",
    "Ext.button.Button",
    "Ext.menu.CheckItem",
    "Ext.menu.Menu",
    "Ext.form.field.ComboBox",
    "Ext.layout.*",
    "Ext.toolbar.Paging",
    "Ext.grid.Panel",
    "Ext.form.field.Date",
    "Ext.form.field.TextArea",
    "Ext.dirac.utils.DiracToolButton",
    "Ext.dirac.utils.DiracApplicationContextMenu",
    "Ext.chart.PolarChart",
  ],

  loadState: function (data) {
    var me = this;

    me.grid.loadState(data);

    me.leftPanel.loadState(data);

    if (data.leftPanelCollapsed) {
      if (data.leftPanelCollapsed) me.leftPanel.collapse();
    }

    if ("centralGridPanelVisible" in data) {
      if (!data.centralGridPanelVisible) {
        me.centralWorkPanel.getLayout().setActiveItem(1);
      }
    }

    if ("statisticsSelectionPanelCollapsed" in data) {
      if (data.statisticsSelectionPanelCollapsed) {
        me.statisticsSelectionGrid.collapse();
      }
    }

    if ("statisticsSelectionValues" in data) {
      me.statisticsGridComboMain.suspendEvents(false);
      me.statisticsGridCombo.suspendEvents(false);
      me.statisticsGridComboMain.setValue(data.statisticsSelectionValues[0]);
      me.statisticsGridCombo.setValue(data.statisticsSelectionValues[1]);
      me.statisticsGridComboMain.resumeEvents();
      me.statisticsGridCombo.resumeEvents();
    }
  },

  getStateData: function () {
    var me = this;

    // data for grid columns
    var oReturn = {
      leftMenu: me.leftPanel.getStateData(),
      grid: me.grid.getStateData(),
      // show/hide for selectors and their selected data (including NOT
      // button)
    };

    oReturn.leftPanelCollapsed = me.leftPanel.collapsed;
    oReturn.centralGridPanelVisible = !me.grid.hidden;
    oReturn.statisticsSelectionPanelCollapsed = me.statisticsSelectionGrid.collapsed;
    oReturn.statisticsSelectionValues = [me.statisticsGridComboMain.getValue(), me.statisticsGridCombo.getValue()];

    return oReturn;
  },
  dataFields: [
    {
      name: "lfn",
    },
    {
      name: "pfn",
    },
    {
      name: "size",
    },
    {
      name: "storageelement",
    },
    {
      name: "guid",
    },
    {
      name: "checksum",
    },
    {
      name: "status",
    },
    {
      name: "startTime",
      type: "date",
      dateFormat: "Y-n-j h:i:s",
    },
    {
      name: "endTime",
      type: "date",
      dateFormat: "Y-n-j h:i:s",
    },
    {
      name: "StatusIcon",
      mapping: "status",
    },
  ],

  initComponent: function () {
    var me = this;

    if (GLOBAL.VIEW_ID == "desktop") {
      me.launcher.title = "RAW Integrity Monitor";
      me.launcher.maximized = false;

      var oDimensions = GLOBAL.APP.MAIN_VIEW.getViewMainDimensions();

      me.launcher.width = oDimensions[0];
      me.launcher.height = oDimensions[1];

      me.launcher.x = 0;
      me.launcher.y = 0;
    }

    if (GLOBAL.VIEW_ID == "tabs") {
      me.launcher.title = "RAW Integrity Monitor";
      me.launcher.maximized = false;

      var oDimensions = GLOBAL.APP.MAIN_VIEW.getViewMainDimensions();

      me.launcher.width = oDimensions[0];
      me.launcher.height = oDimensions[1];

      me.launcher.x = 0;
      me.launcher.y = 0;
    }

    Ext.apply(me, {
      layout: "border",
      bodyBorder: false,
      defaults: {
        collapsible: true,
        split: true,
      },
    });

    me.callParent(arguments);
  },

  buildUI: function () {
    var me = this;

    me.statisticsPanel = new Ext.create("Ext.panel.Panel", {
      header: false,
      region: "center",
      floatable: false,
      // scrollable : true,
      hidden: true,
      collapsible: false,
      layout: "border",
      defaults: {
        collapsible: true,
        split: true,
      },
    });

    /*
     * -----------------------------------------------------------------------------------------------------------
     * DEFINITION OF THE LEFT PANEL
     * -----------------------------------------------------------------------------------------------------------
     */

    var selectors = {
      status: "Status",
      storageelement: "Storage Element",
    };

    var map = [
      ["status", "status"],
      ["storageelement", "storageelement"],
    ];

    var textFields = {
      lfn: {
        name: "LFN",
        type: "string",
      },
    };

    me.leftPanel = Ext.create("Ext.dirac.utils.DiracBaseSelector", {
      scope: me,
      cmbSelectors: selectors,
      datamap: map,
      textFields: textFields,
      url: "RAWIntegrityMonitor/getSelectionData",
    });

    /*
     * -----------------------------------------------------------------------------------------------------------
     * DEFINITION OF THE GRID
     * -----------------------------------------------------------------------------------------------------------
     */

    var oProxy = Ext.create("Ext.dirac.utils.DiracAjaxProxy", {
      url: GLOBAL.BASE_URL + me.applicationName + "/getRawIntegrityData",
    });

    me.dataStore = Ext.create("Ext.dirac.utils.DiracJsonStore", {
      autoLoad: false,
      proxy: oProxy,
      fields: me.dataFields,
      scope: me,
      sorters: [
        {
          property: "lfn",
          direction: "DESC",
        },
      ],
    });

    var pagingToolbar = {};

    var toolButtons = {
      Visible: [
        {
          text: "",
          handler: me.__setActiveItemInTheCentralWorkPanel,
          arguments: [],
          properties: {
            iconCls: "dirac-icon-pie",
            tooltip: "Go to the statistics panel",
          },
        },
      ],
    };

    pagingToolbar = Ext.create("Ext.dirac.utils.DiracPagingToolbar", {
      toolButtons: toolButtons,
      store: me.dataStore,
      scope: me,
    });

    me.btnStatisticsPanel = new Ext.Button({
      text: "",
      iconCls: "dirac-icon-pie",
      tooltip: "Go to the statistics panel",
      handler: function () {
        me.__setActiveItemInTheCentralWorkPanel();
      },
    });

    var menuitems = {
      Visible: [
        {
          text: "Logging Info",
          handler: me.__oprGetLogData,
          properties: {
            tooltip: "Clik to show the loggin info of the file.",
          },
        },
      ],
    };

    me.contextGridMenu = new Ext.dirac.utils.DiracApplicationContextMenu({
      menu: menuitems,
      scope: me,
    });

    var columns = {
      None: {
        dataIndex: "StatusIcon",
        properties: {
          width: 26,
          sortable: false,
          hideable: false,
          fixed: true,
          menuDisabled: true,
        },
        renderFunction: "rendererStatus",
      },
      LFN: {
        dataIndex: "lfn",
      },
      Status: {
        dataIndex: "status",
      },
      PFN: {
        dataIndex: "pfn",
      },
      Size: {
        dataIndex: "size",
      },
      StorageElement: {
        dataIndex: "storageelement",
      },
      GUID: {
        dataIndex: "guid",
      },
      Checksum: {
        dataIndex: "checksum",
      },
      "StartTime [UTC]": {
        dataIndex: "startTime",
        renderer: Ext.util.Format.dateRenderer("Y-m-d H:i:s"),
      },
      "EndTime [UTC]": {
        dataIndex: "endTime",
        renderer: Ext.util.Format.dateRenderer("Y-m-d H:i:s"),
      },
    };

    me.grid = Ext.create("Ext.dirac.utils.DiracGridPanel", {
      store: me.dataStore,
      oColumns: columns,
      contextMenu: me.contextGridMenu,
      pagingToolbar: pagingToolbar,
      scope: me,
    });

    me.leftPanel.setGrid(me.grid);

    me.statisticsGridComboMain = new Ext.form.field.ComboBox({
      allowBlank: false,
      displayField: "set",
      editable: false,
      mode: "local",
      store: new Ext.data.ArrayStore({
        fields: ["set"],
        data: [["Selected Statistics"], ["Global Statistics"]],
      }),
      triggerAction: "all",
      value: "Selected Statistics",
      flex: 1,
      listeners: {
        change: function (combo, newValue, oldValue, eOpts) {
          var me = combo.moduleObject;
          me.leftPanel.oprLoadGridData();
        },
      },
      moduleObject: me,
    });

    me.statisticsGridCombo = new Ext.form.field.ComboBox({
      allowBlank: false,
      displayField: "category",
      editable: false,
      mode: "local",
      store: new Ext.data.ArrayStore({
        fields: ["category"],
        data: [["Status"], ["Storage Element"]],
      }),
      triggerAction: "all",
      value: "Status",
      flex: 1,
      listeners: {
        change: function (combo, newValue, oldValue, eOpts) {
          var me = combo.moduleObject;
          me.leftPanel.oprLoadGridData();
        },
      },
      moduleObject: me,
    });

    var oButtonGoToGrid = new Ext.Button({
      margin: 0,
      iconCls: "pm-grid-icon",
      handler: function () {
        me.centralWorkPanel.getLayout().setActiveItem(0);
      },
      scope: me,
    });

    me.btnShowPlotAsPng = new Ext.Button({
      margin: 0,
      iconCls: "dirac-icon-save",
      handler: function () {
        var plot = me.statisticsPlotPanel.down("chart");

        var domEl = plot.getEl();
        if (domEl && domEl.dom) {
          var sSvgElement = domEl.dom.getElementsByTagName("svg")[0].parentNode.innerHTML;

          var iHeight = me.statisticsPlotPanel.getHeight();

          var iWidth = me.statisticsPlotPanel.getWidth();

          var canvas = document.createElement("canvas");
          canvas.setAttribute("width", iWidth);
          canvas.setAttribute("height", iHeight);

          var oContext = canvas.getContext("2d");

          oContext.beginPath();
          oContext.rect(0, 0, iWidth, iHeight);
          oContext.fillStyle = "#FFFFFF";
          oContext.fill();

          var oImage = new Image();
          oImage.src = GLOBAL.ROOT_URL + "static/core/img/wallpapers/dirac_jobmonitor_background.png";

          oImage.onload = function () {
            console.log([oImage.clientWidth, oImage.clientHeight]);

            oContext.drawImage(oImage, 0, 0, iWidth, iHeight);

            oContext.drawSvg(sSvgElement, 0, 0);

            var imgData = canvas.toDataURL("image/png");
            window.location = imgData.replace("image/png", "image/octet-stream");
          };
        } else {
          plot.save({
            type: "image/png",
            src: GLOBAL.ROOT_URL + "static/core/img/wallpapers/dirac_jobmonitor_background.png",
            backround: GLOBAL.ROOT_URL + "static/core/img/wallpapers/dirac_jobmonitor_background.png",
            cls: GLOBAL.ROOT_URL + "static/core/img/wallpapers/dirac_jobmonitor_background.png",
          });
        }
      },
      scope: me,
      tooltip: "Save pie chart as PNG image",
    });

    me.btnPlotSettings = new Ext.Button({
      margin: 0,
      iconCls: "dirac-icon-pie",
      handler: function () {
        me.formPlotSettings();
      },
      scope: me,
      tooltip: "Plot settings",
    });

    /*-----------AUTO REFRESH---------------*/
    var oTask = {
      run: function () {
        me.leftPanel.oprLoadGridData();
      },
      interval: 0,
    };

    var oHeartbeat = new Ext.util.TaskRunner();

    var oAutoMenu = [
      {
        handler: function () {
          this.setChecked(true);
          oHeartbeat.start(
            Ext.apply(oTask, {
              interval: 900000,
            })
          );
        },
        group: "refresh",
        text: "15 Minutes",
      },
      {
        handler: function () {
          this.setChecked(true);
          oHeartbeat.start(
            Ext.apply(oTask, {
              interval: 1800000,
            })
          );
        },
        group: "refresh",
        text: "30 Minutes",
      },
      {
        handler: function () {
          this.setChecked(true);
          oHeartbeat.start(
            Ext.apply(oTask, {
              interval: 3600000,
            })
          );
        },
        group: "refresh",
        text: "One Hour",
      },
      {
        checked: true,
        handler: function () {
          this.setChecked(true);
          oHeartbeat.stopAll();
        },
        group: "refresh",
        text: "Disabled",
      },
    ];

    for (var i = 0; i < oAutoMenu.length; i++) {
      oAutoMenu[i] = new Ext.menu.CheckItem(oAutoMenu[i]);
    }

    var btnAutorefresh = new Ext.Button({
      menu: oAutoMenu,
      text: "Auto Refresh: Disabled",
      tooltip: "Click to set the time for autorefresh",
    });

    btnAutorefresh.on("menuhide", function (button, menu) {
      var length = menu.items.getCount();
      for (var i = 0; i < length; i++) {
        if (menu.items.items[i].checked) {
          button.setText("Auto Refresh: " + menu.items.items[i].text);
        }
      }
    });

    var oColumns = {
      None: {
        dataIndex: "key",
        properties: {
          width: 26,
          sortable: false,
          hideable: false,
          fixed: true,
          menuDisabled: true,
        },
        renderFunction: "rendererStatus",
      },
      Key: {
        dataIndex: "key",
        properties: {
          hideable: false,
          width: 150,
        },
      },
      Value: {
        dataIndex: "value",
        properties: {
          flex: 1,
        },
        renderFunction: "diffValues",
      },
    };

    var dataStore = Ext.create("Ext.dirac.utils.DiracArrayStore", {
      fields: ["key", "value", "code", "color"],
      oDiffFields: {
        Id: "key",
        Fields: ["value"],
      },
      scope: me,
    });

    /*---------------------------------------------------*/
    me.statisticsSelectionGrid = Ext.create("Ext.dirac.utils.DiracGridPanel", {
      region: "west",
      store: dataStore,
      width: 300,
      header: false,
      border: 0,
      viewConfig: {
        stripeRows: true,
        enableTextSelection: true,
      },
      dockedItems: [
        new Ext.create("Ext.toolbar.Toolbar", {
          dock: "top",
          items: [oButtonGoToGrid, me.btnShowPlotAsPng, me.btnPlotSettings, "-", btnAutorefresh],
        }),
        new Ext.create("Ext.toolbar.Toolbar", {
          dock: "top",
          items: [me.statisticsGridComboMain],
        }),
        new Ext.create("Ext.toolbar.Toolbar", {
          dock: "top",
          items: [me.statisticsGridCombo],
        }),
      ],
      oColumns: oColumns,
      scope: me,
    });

    me.plotSettings = {};

    me.plotSettings.plotTitle = {
      type: "text",
      text: "No data",
      font: "18px Helvetica",
      width: 100,
      height: 30,
      x: 40, // the sprite x position
      y: 12,
      // the sprite y position
    };
    me.plotSettings.plotLegend = {
      field: "key",
      position: "right",
      boxStrokeWidth: 2,
      labelFont: "12px Helvetica",
      padding: 10,
    };

    me.statisticsPlotPanel = new Ext.create("Ext.panel.Panel", {
      region: "center",
      floatable: false,
      layout: "fit",
      header: false,
    });

    me.statisticsPlotPanel.onResize = function (width, height, oldWidth, oldHeight) {
      me.createPlotFromGridData(me.statisticsGridComboMain.getValue() + " :: " + me.statisticsGridCombo.getValue());
    };

    me.statisticsPanel.add([me.statisticsSelectionGrid, me.statisticsPlotPanel]);

    /* END - Definition of the statistics panel */

    /*
     * -----------------------------------------------------------------------------------------------------------
     * DEFINITION OF THE MAIN CONTAINER
     * -----------------------------------------------------------------------------------------------------------
     */

    me.centralWorkPanel = new Ext.create("Ext.panel.Panel", {
      floatable: false,
      layout: "card",
      region: "center",
      header: false,
      border: false,
      items: [me.grid, me.statisticsPanel],
    });

    /*
     * -----------------------------------------------------------------------------------------------------------
     * DEFINITION OF THE MAIN CONTAINER
     * -----------------------------------------------------------------------------------------------------------
     */
    me.add([me.leftPanel, me.centralWorkPanel]);
    // me.add([me.leftPanel, me.grid]);
  },

  __oprGetLogData: function () {
    var me = this;
    var lfn = GLOBAL.APP.CF.getFieldValueFromSelectedRow(me.grid, "lfn");

    me.getContainer().body.mask("Wait ...");

    Ext.Ajax.request({
      url: GLOBAL.BASE_URL + "RAWIntegrityMonitor/getloggingInfo",
      method: "POST",
      params: {
        lfn: Ext.JSON.encode([lfn]),
      },
      scope: me,
      success: function (response) {
        me.getContainer().body.unmask();
        var jsonData = Ext.JSON.decode(response.responseText);

        if (jsonData["success"] == "true") {
          me.getContainer().oprPrepareAndShowWindowGrid(
            jsonData["result"],
            "Logging onfo for:" + lfn,
            ["status", "minorstatus", "statustime", "source"],
            [
              {
                text: "Status",
                flex: 1,
                sortable: false,
                dataIndex: "status",
              },
              {
                text: "Minor Status",
                flex: 1,
                sortable: false,
                dataIndex: "minorstatus",
              },
              {
                text: "Status Time",
                flex: 1,
                sortable: false,
                dataIndex: "statustime",
              },
              {
                text: "Source",
                flex: 1,
                sortable: false,
                dataIndex: "source",
              },
            ]
          );
        } else {
          GLOBAL.APP.CF.alert(jsonData["error"], "error");
        }
      },
    });
  },

  __setActiveItemInTheCentralWorkPanel: function () {
    var me = this;
    me.centralWorkPanel.getLayout().setActiveItem(1);
  },
  createPlotFromGridData: function (sTitle, sLegendPosition) {
    var me = this;
    me.statisticsPlotPanel.removeAll();
    if (!sLegendPosition) {
      if ("plotSettings" in me && "plotLegend" in me.plotSettings) {
        sLegendPosition = me.plotSettings.plotLegend.legend;
      } else {
        sLegendPosition = "right";
      }
    }

    var oNow = new Date();

    me.plotSettings.plotTitle.text = sTitle + " (" + oNow.toString() + ")";
    me.plotSettings.plotLegend.position = sLegendPosition;

    var plot = Ext.create("Ext.chart.PolarChart", {
      height: 410,
      padding: "10 0 0 0",
      cls: "jm-statistics-plot-background",
      animate: true,
      shadow: false,
      store: me.statisticsSelectionGrid.getStore(),
      insetPadding: 40,
      legend: me.plotSettings.plotLegend,
      theme: "Base:gradients",
      items: [me.plotSettings.plotTitle],
      series: [
        {
          type: "pie",
          cls: "jm-statistics-plot-background",
          angleField: "value",
          label: {
            field: "key",
            display: "outside",
            calloutLine: true,
          },
          showInLegend: true,
          highlight: {
            segment: {
              margin: 20,
            },
          },
          tips: {
            width: 140,
            height: 28,
            trackMouse: true,
            renderer: function (storeItem, item) {
              this.setTitle(storeItem.get("key") + ": " + storeItem.get("value"));
            },
          },
        },
      ],
    });
    me.statisticsPlotPanel.add(plot);
  },
  formPlotSettings: function () {
    var me = this;

    if (me.plotSettings === undefined) me.plotSettings = {};

    me.plotSettings.txtPlotTitle = Ext.create("Ext.form.field.Text", {
      fieldLabel: "Title",
      labelAlign: "left",
      allowBlank: false,
      margin: 10,
      anchor: "100%",
      value: me.plotSettings.plotTitle.text,
    });

    me.plotSettings.cmbLegendPosition = new Ext.create("Ext.form.field.ComboBox", {
      labelAlign: "left",
      fieldLabel: "Legend position",
      store: new Ext.data.ArrayStore({
        fields: ["value", "text"],
        data: [
          ["right", "right"],
          ["left", "left"],
          ["top", "top"],
          ["bottom", "bottom"],
          ["none", "none"],
        ],
      }),
      displayField: "text",
      valueField: "value",
      anchor: "100%",
      margin: 10,
      value: me.plotSettings.plotLegend.legend,
    });

    // button for saving the state
    me.plotSettings.btnApplySettings = new Ext.Button({
      text: "Submit",
      margin: 3,
      iconCls: "dirac-icon-submit",
      handler: function () {
        var me = this;
        me.createPlotFromGridData(me.plotSettings.txtPlotTitle.getValue(), me.plotSettings.cmbLegendPosition.getValue());
      },
      scope: me,
    });

    var oToolbar = new Ext.toolbar.Toolbar({
      border: false,
    });

    oToolbar.add([me.plotSettings.btnApplySettings]);

    var oPanel = new Ext.create("Ext.panel.Panel", {
      autoHeight: true,
      border: false,
      layout: "anchor",
      items: [oToolbar, me.plotSettings.txtPlotTitle, me.plotSettings.cmbLegendPosition, me.txtElementConfig],
    });

    // initializing window showing the saving form
    Ext.create("widget.window", {
      height: 300,
      width: 500,
      title: "Plot Settings",
      layout: "fit",
      modal: true,
      items: oPanel,
    }).show();
  },

  funcOnChangeEitherCombo: function () {
    var me = this;

    var sSet = me.statisticsGridComboMain.getValue();
    var sCategory = me.statisticsGridCombo.getValue();

    me.statisticsGridComboMain.setDisabled(true);
    me.statisticsGridCombo.setDisabled(true);

    if (sSet == "Selected Statistics") {
      var oData = me.leftPanel.getSelectionData();
      oData.statsField = sCategory;

      me.statisticsSelectionGrid.body.mask("Wait ...");

      Ext.Ajax.request({
        url: GLOBAL.BASE_URL + me.applicationName + "/getStatisticsData",
        params: oData,
        scope: me,
        success: function (response) {
          var response = Ext.JSON.decode(response.responseText);

          if (response["success"] == "true") {
            me.statisticsSelectionGrid.store.removeAll();

            me.statisticsSelectionGrid.store.add(response["result"]);

            me.createPlotFromGridData(sSet + " :: " + sCategory);
          } else {
            GLOBAL.APP.CF.alert(response["error"], "error");
          }

          me.statisticsSelectionGrid.body.unmask();
          me.statisticsGridComboMain.setDisabled(false);
          me.statisticsGridCombo.setDisabled(false);
        },
        failure: function (response) {
          me.statisticsGridComboMain.setDisabled(false);
          me.statisticsGridCombo.setDisabled(false);
          me.statisticsSelectionGrid.body.unmask();
          GLOBAL.APP.CF.showAjaxErrorMessage(response);
        },
      });
    } else {
      me.statisticsSelectionGrid.body.mask("Wait ...");

      Ext.Ajax.request({
        url: GLOBAL.BASE_URL + me.applicationName + "/getStatisticsData",
        params: {
          statsField: sCategory,
          globalStat: true,
        },
        scope: me,
        success: function (response) {
          var response = Ext.JSON.decode(response.responseText);

          if (response["success"] == "true") {
            me.statisticsSelectionGrid.store.removeAll();

            me.statisticsSelectionGrid.store.add(response["result"]);

            me.createPlotFromGridData(sSet + " :: " + sCategory);
          } else {
            GLOBAL.APP.CF.alert(response["error"], "error");
          }
          me.statisticsSelectionGrid.body.unmask();
          me.statisticsGridComboMain.setDisabled(false);
          me.statisticsGridCombo.setDisabled(false);
        },
        failure: function (response) {
          me.statisticsSelectionGrid.body.unmask();
          me.statisticsGridComboMain.setDisabled(false);
          me.statisticsGridCombo.setDisabled(false);
          GLOBAL.APP.CF.showAjaxErrorMessage(response);
        },
      });
    }
  },
});
