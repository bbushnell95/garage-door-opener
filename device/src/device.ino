/*
 * Project device
 * Description: Device for opening garage door
 * Author: Brett Bushnell (brettbushnell95@gmail.com)
 * Date: 4/1/2018
 */

using namespace std;

void responseHandler(const char *event, const char *data){
    String response = String::format("POST response:\n %s\n %s\n", event, data);
    Serial.println(response);
}
// setup() runs once, when the device is first turned on.
void setup() {
  // Put initialization like pinMode and begin functions here.
    Serial.begin(115200);

    //Sync the particle time with the cloud
    Particle.syncTime();

    //Subscripe to webhook
    Particle.subscribe("hook-response/status", responseHandler, MY_DEVICES);
    pinMode(D7, OUTPUT);
}

// loop() runs over and over again, as quickly as it can execute.
void loop() {
  // The core of your code will likely live here.
    String postData;
    // Confirm D7 is low
    digitalWrite(D7, LOW);
    delay(1000);
    postData = String::format("{\"door_state\": \"open\"}");
    Serial.println(postData);
    // Publish the data to the webhook
    Particle.publish("status", postData);
    // Set pin to high to notify a succesful send
    digitalWrite(D7, HIGH);
    // Delay 1 second
    delay(1000);
}
