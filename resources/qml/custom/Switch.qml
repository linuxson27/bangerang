import QtQuick 2.13
import QtQuick.Controls 2.13

Switch {
    id: control

    indicator: Rectangle {
        implicitWidth: 40
        implicitHeight: 20
        x: control.leftPadding
        y: parent.height / 2 - height / 2
        radius: 10
        color: control.checked ? "crimson" : "grey"

        Rectangle {
            x: control.checked ? parent.width - width - 3 : 3
            anchors.verticalCenter: parent.verticalCenter
            width: 14
            height: 14
            radius: 7
            color: "#191919"
        }
    }

    contentItem: Text {
        text: control.text
        font.family: "Roboto"
        font.pixelSize: 18
        color: "grey"
        verticalAlignment: Text.AlignVCenter
        leftPadding: control.indicator.width + control.spacing
    }
}