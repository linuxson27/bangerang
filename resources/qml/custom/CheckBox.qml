import QtQuick 2.13
import QtQuick.Controls 2.13

CheckBox {
    id: ctrl
    indicator: Rectangle {
        implicitWidth: 16
        implicitHeight: 16
        x: ctrl.leftPadding
        y: parent.height / 2 - height / 2

        Image {
            width: 16
            height: 16
            anchors.centerIn: parent
            visible: remember_me.checked
            source: "../../img/check.svg"
        }
    }

    contentItem: Text {
        text: ctrl.text
        font.pixelSize: 12
        color: "white"
        verticalAlignment: Text.AlignVCenter
        leftPadding: ctrl.indicator.width + ctrl.spacing
    }
}