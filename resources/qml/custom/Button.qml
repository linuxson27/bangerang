import QtQuick 2.13
import QtQuick.Controls 2.13
import QtQuick.Layouts 1.13


Button {
	id: ctrl

	property color bg_color: "white"
	property color txt_color: "black"
	property int font_size: 18
	property int b_width: 0
	property real b_radius: 0
	property color b_color: "transparent"
	property bool a_true: false
	property string icon_source: ""
	property bool show_icon: false
	property real icon_opacity: 1
	property bool show_text: true
	property int btn_id: 0
	property int content_spacing: 0
	property string pressed_border: "dodgerblue"
	property string highlight_border: "crimson"

	background: Rectangle {
		border.width: b_width
		border.color: b_color
		radius: b_radius
		antialiasing: a_true
		color: bg_color

		Rectangle { // Animated darker touch/click
			id: bg
			color: Qt.darker(bg_color, 1.25)
			anchors.centerIn: parent
			radius: width / 2
		}

		Rectangle { // Border on active highlight
			anchors.fill: parent
			border.width: ctrl.activeFocus ? 1 : 0
			border.color: highlight_border
			color: "transparent"
		}

		Rectangle { // Border on press
			anchors.fill: parent
			border.width: ctrl.down ? 1 : 0
			border.color: pressed_border
			color: "transparent"
		}
	}
	onPressed: ctrl.state = "button pressed";
	onReleased: ctrl.state = "button inactive";
	clip: true

	contentItem: Item {
		anchors.fill: parent

		MouseArea {
			anchors.fill: parent
			propagateComposedEvents: true
			hoverEnabled: true

			onClicked: mouse.accepted =false;
			onPressed: mouse.accepted = false;
			onReleased: mouse.accepted = false;
			onDoubleClicked: mouse.accepted = false;
			onPositionChanged: mouse.accepted = false;
			onPressAndHold: mouse.accepted = false;
			onExited: ctrl.pressed ? ctrl.state = "button inactive" : ctrl.state = "button inactive"
		}

		Column {
			anchors.centerIn: parent
			spacing: content_spacing

			Image {
				id: icon
				width: sourceSize.width
				height: sourceSize.height
				anchors.horizontalCenter: parent.horizontalCenter
				source: icon_source
				fillMode: Image.PreserveAspectFit
				visible: show_icon
				opacity: icon_opacity
			}

			Text {
				id: text
				width: ctrl.width - (ctrl.leftPadding + ctrl.rightPadding)
				anchors.horizontalCenter: parent.horizontalCenter
				text: ctrl.text
				padding: 0
				horizontalAlignment: Text.AlignHCenter
				verticalAlignment: Text.AlignVCenter
				font.pixelSize: font_size
				lineHeight: 0.80
				color: txt_color
				wrapMode: Text.WordWrap
				visible: show_text
			}
		}
	}


	states: [
		State {
			name: "button inactive"
			PropertyChanges {
				target: bg
				width: 0
				height: 0
			}
		},
		State {
			name: "button pressed"
			PropertyChanges {
				target: bg
				width: ctrl.width * 2
				height: ctrl.width * 2
			}
		}
	]
	state: "button inactive"
	transitions: [
		Transition {
			from: "button inactive"
			to: "button pressed"
			NumberAnimation { properties: "width, height"; duration: 150 }
		},
		Transition {
			from: "button pressed"
			to: "button inactive"
			NumberAnimation { properties: "width, height"; duration: 150 }
		}
	]
}