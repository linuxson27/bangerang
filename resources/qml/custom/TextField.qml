import QtQuick 2.13
import QtQuick.Controls 2.13
import QtQuick.Layouts 1.13


TextField { // Customized input field
	id: inp

	property string placeholder_text: ""
	property string font_family: "Roboto"
	property int font_size: 18
	property color font_color: "white"
	property int u_thickness: 2
	property color u_color: "dodgerblue"
	property bool show_del_btn: false

	font.family: font_family
	font.pixelSize: font_size
	color: font_color
	onFocusChanged: {
		focus || !inp.text ? inp.state = "input is active" : null;
		!focus || !inp.text ? inp.state = "input is inactive": null;
		focus || inp.text ? inp.state = "input is active" : null;

		// Testing error state only
		focus && inp.text === "error" ? inp.state = "input error" : null
		!focus && inp.text === "error" ? inp.state = "input error" : null
	}
	
	MouseArea {
		id: inputMA
		width: parent.width - 20
		height: parent.height
		onEntered: { inp.state = "input is active"; inp.forceActiveFocus() }
	}

	MouseArea {
		id: btnMA
		width: 20
		height: parent.height
		anchors.right: parent.right
		onClicked: { inp.forceActiveFocus(); inp.clear() }
		cursorShape: Qt.PointingHandCursor
	}

	background: Item {
		anchors.fill: parent

		Rectangle {
			id: underline
			width: parent.width
			height: 1
			anchors.bottom: parent.bottom
			color: "grey"
		}

		Rectangle {
			visible: inp.focus
			id: activeUnderline
			width: 0
			height: u_thickness
			anchors.bottom: parent.bottom
			color: u_color
		}

		Label { // Placeholder text which animates to top of input when active
			id: hoverText
			anchors.left: parent.left
			anchors.leftMargin: 10
			font.family: font_family
			font.pixelSize: font_size
			color: "grey"
			text: placeholder_text
		}

		Label { // Error msg below input field
			id: errorMsg
			visible: false
			anchors.left: parent.left
			anchors.leftMargin: 10
			anchors.top: parent.bottom
			anchors.topMargin: 5
			font.family: font_family
			font.pixelSize: font_size
			color: "red"
			text: ""
		}

		Rectangle { // Delete button
			visible: show_del_btn
			id: inputDelBtn
			width: 24
			height: 24
			anchors.right: parent.right
			anchors.verticalCenter: parent.verticalCenter
			color: { btnMA.pressed ? Qt.darker("#191919", 1.25) : "#191919" }
			radius: width / 2
			antialiasing: true

			Image {
				width: 10
				height: 10
				anchors.centerIn: parent
				source: "../../img/close.svg"
				antialiasing: true
			}
		}

		Item {
			width: 16
			height: 16
			anchors.verticalCenter: parent.verticalCenter

			Image {
				id: errIcon
				opacity: 0.0
				anchors.fill: parent
				source: "../../img/warning.svg"
			}
		}
	}

	states: [
		State {
			name: "input is inactive"
			PropertyChanges {
				target: hoverText
				font.pixelSize: font_size
				y: 8
			}
			PropertyChanges {
				target: inputDelBtn
				opacity: 0.0
			}
		},
		State {
			name: "input is active"
			PropertyChanges {
				target: hoverText
				font.pixelSize: 12
				y: -10
			}
			PropertyChanges {
				target: activeUnderline
				width: parent.width
			}
			PropertyChanges {
				target: inputDelBtn
				opacity: 1.0
			}
		},
		State {
			name: "input error"
			PropertyChanges {
				target: inp
				leftPadding: 25
			}
			PropertyChanges {
				target: hoverText
				font.pixelSize: 12
				y: -10
				color: "red"
			}
			PropertyChanges {
				target: activeUnderline
				width: parent.width
				color: "red"
			}
			PropertyChanges {
				target: errIcon
				opacity: 1.0
			}
		}
	]

	state: "input is inactive"
	transitions: [
		Transition {
			from: "input is inactive"
			to: "input is active"
			NumberAnimation { properties: "font.pixelSize, y, width, opacity"; duration: 100 }
		},
		Transition {
			from: "input is active"
			to: "input is inactive"
			NumberAnimation { properties: "font.pixelSize, y, width, opacity"; duration: 100 }
		},
		Transition {
			from: "input is active"
			to: "input error"
			NumberAnimation { properties: "leftPadding, opacity"; duration: 100 }
		}
	]
}