import QtQuick 2.13
import QtQuick.Controls 2.13
import QtQuick.Layouts 1.13
import QtGraphicalEffects 1.14
// import QtMultimedia 5.13


Button {
	id: ctrl
	clip: true
	onPressed: {
		ctrl.state == "button inactive" ? ctrl.state = "button active" : ctrl.state = "button inactive";
		// button_sound.play();
	}

	property real border_radius: ctrl.width / 10
	property bool show_text: true
	property color txt_color: "#9D9D9D"
	property int font_size: 12
	property bool show_icon: false
	property string icon_source: ""
	property int content_spacing: 0

	// SoundEffect {
	// 	id: button_sound
	// 	source: "../../sounds/button.wav"
	// }
	
	background: Rectangle { // Main container
		id: container
		anchors.fill: parent
		color: "transparent"

		Rectangle { // Dropshadow container and highlight border
			id: border
			width: parent.width - 2
			height: parent.height - 2
			anchors.centerIn: parent
			radius: border_radius
			visible: false
			antialiasing: true
			gradient: Gradient {
				GradientStop { position: 0.0; color: "#404040" }
				GradientStop { position: 1.0; color: "#1E1E1E" }
			}

			Rectangle { // Button fill
				id: bg
				width: parent.width - 2
				height: parent.height - 2
				anchors.centerIn: parent
				radius: border_radius - 4

				RadialGradient {
					anchors.fill: parent
					source: bg
					gradient: Gradient {
						GradientStop { position: 0.0; color: "#3B3B3B" }
						GradientStop { position: 0.5; color: "#2A2A2A" }
					}
				}
			}
		}

		DropShadow { // Button shadow
			anchors.fill: parent
			horizontalOffset: 1
			verticalOffset: 1
			radius: 8.0
			samples: 17
			color: "#50000000"
			source: border
		}
	}
	contentItem: Item {
		anchors.fill: parent

		Column { // Content container
			anchors.centerIn: parent
			spacing: content_spacing

			Image {
				id: icon
				width: sourceSize.width
				height: sourceSize.height
				anchors.horizontalCenter: parent.horizontalCenter
				source: icon_source + ".svg"
				fillMode: Image.PreserveAspectFit
				visible: show_icon
				smooth: true

				Glow {
					id: icon_glow
					anchors.fill: icon
					radius: 4
					samples: 9
					source: icon
				}
			}

			Text {
				id: text
				width: ctrl.width - (ctrl.leftPadding + ctrl.rightPadding)
				anchors.horizontalCenter: parent.horizontalCenter
				text: ctrl.text
				padding: 0
				horizontalAlignment: Text.AlignHCenter
				font.pixelSize: font_size
				lineHeight: 0.80
				color: txt_color
				wrapMode: Text.WordWrap
				visible: show_text

				Glow {
					id: text_glow
					anchors.fill: text
					radius: 1
					samples: 3
					source: text
				}
			}
		}
	}
	states: [
		State {
			name: "button inactive"
			PropertyChanges {
				target: icon
				source: icon_source + ".svg"
			}
			PropertyChanges {
				target: icon_glow
				color: "transparent"
			}
			PropertyChanges {
				target: text_glow
				color: "transparent"
			}
		},
		State {
			name: "button active"
			PropertyChanges {
				target: icon
				source: icon_source + "_active.svg"
			}
			PropertyChanges {
				target: icon_glow
				color: "#501e90ff"
			}
			PropertyChanges {
				target: text
				color: "dodgerblue"
			}
			PropertyChanges {
				target: text_glow
				color: "#501e90ff"
			}
		}
	]
	state: "button inactive"
}