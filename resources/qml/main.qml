import QtQuick 2.13
import QtQuick.Controls 2.13
import QtQuick.Layouts 1.13
import "custom"


ApplicationWindow {
	visible: true
	width: 350
	height: 250
	color: '#191919'
    Component.onCompleted: Bangerang.check_update();

	StackView { // Main container for all pages
		id: view
		anchors.fill: parent
		initialItem: add_profile
	}

    Component { // Splash screen
        id: splash

		Item { // Container
			Layout.fillWidth: true
			Layout.fillHeight: true
            Component.onCompleted: loading_timer.running = true;

            Timer { // Loading label state animation timer
                id: loading_timer
                interval: 1500
                running: false
                repeat: false
                onTriggered: { 
                    loading.state = "loading fade end";
                    busy_timer.running = true;
                }
            }

            Timer { // Busy indicator state animation timer (after label)
                id: busy_timer
                interval: 500
                running: false
                repeat: false
				onTriggered: {
					busyIndicator.state = "busy fade end";
				}
            }

			Image { // Logo
				id: logo
				width: 155
				height: 38
				anchors.centerIn: parent
				fillMode: Image.PreserveAspectFit
				antialiasing: true
				source: "../img/logo.svg"
				states: [
					State {
						name: "logo fade-in start"
						PropertyChanges { target: logo; opacity: 0 }
					},
					State {
						name: "logo fade-in end"
						when: logo.status == Image.Ready
						PropertyChanges { target: logo; opacity: 1 }
					}
				]
				state: "logo fade-in start"
				transitions: [
					Transition {
						from: "logo fade-in start"
						to: "logo fade-in end"
						NumberAnimation { property: "opacity"; duration: 500 }
					}
				]
			}

            Label { // Loading label
                id: loading
                anchors.right: parent.right
                anchors.rightMargin: 40
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 15
                text: "loading"

                states: [
                    State {
                        name: "loading fade start"
                        PropertyChanges { target: loading; anchors.rightMargin: 0; opacity: 0 }
                    },
                    State {
                        name: "loading fade end"
                        PropertyChanges { target: loading; anchors.rightMargin: 40; opacity: 1 }
                    }
                ]
                state: "loading fade start"
                transitions: [
                    Transition {
                        from: "loading fade start"
                        to: "loading fade end"
                        NumberAnimation { 
                            properties: "anchors.rightMargin, opacity"
                            duration: 500
                            easing.type: Easing.InOutBack
                        }
                    }
                ]
            }

            BusyIndicator { // Busy indicator
                id: busyIndicator
                anchors.verticalCenter: loading.verticalCenter
                anchors.right: parent.right
                anchors.rightMargin: 5
                
                contentItem: Image {
                    width: 24
                    height: 24
                    fillMode: Image.PreserveAspectFit
                    antialiasing: true
                    source:"../img/loading_small.svg"
                    RotationAnimator on rotation {
                        running: true
                        loops: Animation.Infinite
                        duration: 1000
                        from: 0; to: 360
                    }
                }
                states: [
                    State {
                        name: "busy fade start"
                        PropertyChanges { target: busyIndicator; opacity: 0 }
                    },
                    State {
                        name: "busy fade end"
                        PropertyChanges { target: busyIndicator; opacity: 1 }
                    }
                ]
                state: "busy fade start"
                transitions: [
                    Transition {
                        from: "busy fade start"
                        to: "busy fade end"
                        NumberAnimation { properties: "opacity"; duration: 500 }
                    }
                ]
            }
		}
    }

    Component { // Shows before show_profiles if config shows no users
        id: add_profile

        Item { // Container
            ColumnLayout {
                anchors.centerIn: parent
                spacing: 10

                Label {
                    font.pixelSize: 48
                    text: "add profile"
                }

                Label {
                    Layout.topMargin: -10
                    font.pixelSize: 18
                    text: "add a profile for another person watching bangerang"
                    color: "grey"
                }

                Rectangle { // Separator
                    Layout.fillWidth: true
                    Layout.preferredHeight: 1
                    color: "grey"
                }

                Item { // New profile form container
                    Layout.fillWidth: true
                    Layout.preferredHeight: childrenRect.height
                    Layout.topMargin: 20
                    Layout.bottomMargin: 20

                    Button {
                        id: profile_icon
                        width: 80
                        height: 80
                        bg_color: "#191919"
                        b_width: 1
                        b_color: "grey"
                        pressed_border: "grey"
                        highlight_border: "transparent"
                        show_text: false
                        show_icon: true
                        icon_source: "../../img/smiley.svg"
                        icon_opacity: 0.25
                    }

                    Item { // Form controls container
                        anchors.left: profile_icon.right
                        anchors.leftMargin: 20

                        TextField {
                            width: 220
                            anchors.left: parent.left
                            placeholder_text: "name"
                            show_del_btn: true
                        }
                    }
                }

                Rectangle { // Separator
                    Layout.fillWidth: true
                    Layout.preferredHeight: 1
                    color: "grey"
                }
            }
        }
    }

    Component {
        id: show_profiles

        Item { // Container

        }
    }

	Connections {
		target: Bangerang

		//001
		onFinished_loading: {
			if (callback == "current") {
				console.log("App is up to date!");
			} else {
                console.log("Up is outdated, please update");
				// loading_label = false;
				// updatePopup.open();
			}
		}
	}
}