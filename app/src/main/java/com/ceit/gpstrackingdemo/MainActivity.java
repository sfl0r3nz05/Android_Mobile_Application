package com.ceit.gpstrackingdemo;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;

import android.Manifest;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.location.Address;
import android.location.Geocoder;
import android.location.Location;
import android.os.Build;
import android.os.Bundle;
import android.os.PowerManager;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.View;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.Switch;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.location.FusedLocationProviderClient;
import com.google.android.gms.location.LocationCallback;
import com.google.android.gms.location.LocationRequest;
import com.google.android.gms.location.LocationResult;
import com.google.android.gms.location.LocationServices;
import com.google.android.gms.location.Priority;
import com.google.android.gms.tasks.OnSuccessListener;

import com.ceit.gpstrackingdemo.GnssContainer;
import com.ceit.gpstrackingdemo.ServerCommunicationThread;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class MainActivity extends AppCompatActivity {

    public static final int DEFAULT_UPDATE_INTERVAL = 30;
    public static final int FAST_UPDATE_INTERVAL = 5;
    private static final int PERMISSIONS_FINE_LOCATION = 99;
    TextView tv_lat, tv_lon, tv_altitude, tv_accuracy, tv_speed, tv_sensor, tv_updates, tv_address, tv_wayPointCounts, tv_navMessage;
    Switch sw_locationupdates, sw_gps;
    Button btnEmpezar;

    //Variable to remember if we are tracking location or not.
    boolean updateOn = false;
    //current location
    Location currentLocation;
    //list of saved locations
    List<Location> savedLocations;
    //Location request is a config file for all settings related to FusedLocationProviderClient
    LocationRequest locationRequest;
    LocationRequest.Builder locationRequest2;
    LocationRequest.Builder locReqBuilder;
    //Google's API for location services. The majority of the app functions using this class.
    FusedLocationProviderClient fusedLocationProviderClient;
    LocationCallback locationCallBack;
    private GnssContainer mGpsContainer;

    Socket socket;
    private ExecutorService executorService;
//    ServerCommunicationThread thread;
    Boolean threadStatus;
    PythonExecutionThread pythonThread;

    PowerManager powerManager;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);

        tv_lat = findViewById(R.id.tv_lat);
        tv_lon = findViewById(R.id.tv_lon);
        tv_altitude = findViewById(R.id.tv_altitude);
        tv_accuracy = findViewById(R.id.tv_accuracy);
        tv_speed = findViewById(R.id.tv_speed);
        tv_sensor = findViewById(R.id.tv_sensor);
        tv_updates = findViewById(R.id.tv_updates);
        tv_address = findViewById(R.id.tv_address);
        tv_wayPointCounts = findViewById(R.id.tv_countOfCrumbs);
        sw_gps = findViewById(R.id.sw_gps);
        sw_locationupdates = findViewById(R.id.sw_locationsupdates);
        tv_navMessage = findViewById(R.id.tv_navMessage);
        btnEmpezar = findViewById(R.id.btn_empezar);

        pythonThread = new PythonExecutionThread(this);
        pythonThread.start();

        //probar a crear el GnssContainer antes de nada
//        mGpsContainer = new GnssContainer(MainActivity.this, tv_navMessage);
        mGpsContainer = new GnssContainer(MainActivity.this);

//        thread = new ServerCommunicationThread("10.63.140.75");
//        thread = new ServerCommunicationThread("192.168.137.1");
//        thread = new ServerCommunicationThread("localhost");
//        thread.start();
//
//        threadStatus = thread.isAlive();

        btnEmpezar.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                endMessage();
            }
        });

        //to keep the app running even with screen off
        //need to change battery manager manually to 'no restrictions'
        powerManager = (PowerManager) getSystemService(POWER_SERVICE);
        PowerManager.WakeLock wakeLock = powerManager.newWakeLock(PowerManager.PARTIAL_WAKE_LOCK,
                "MyApp::MyWakelockTag");
        wakeLock.acquire();


        //set all properties of locationRequest
//        locReqBuilder = new LocationRequest.Builder(Priority.PRIORITY_HIGH_ACCURACY,1000 * DEFAULT_UPDATE_INTERVAL);
//        locReqBuilder.setMinUpdateIntervalMillis(1000 * FAST_UPDATE_INTERVAL);
//        locationRequest = locReqBuilder.build();
        locationRequest =  new LocationRequest.Builder(Priority.PRIORITY_HIGH_ACCURACY,1000 * DEFAULT_UPDATE_INTERVAL)
                .setMinUpdateIntervalMillis(1000 * FAST_UPDATE_INTERVAL)
                .build();
//        locationRequest = new LocationRequest();
//        locationRequest.setInterval(1000 * DEFAULT_UPDATE_INTERVAL);
//        locationRequest.setFastestInterval(1000 * FAST_UPDATE_INTERVAL);
//        locationRequest.setPriority(LocationRequest.PRIORITY_BALANCED_POWER_ACCURACY);

        //event that is triggered whenever the update interval is met
        locationCallBack = new LocationCallback() {
            @Override
            public void onLocationResult(@NonNull LocationResult locationResult) {
                super.onLocationResult(locationResult);
                //save the location
                updateUIValues(locationResult.getLastLocation());
            }
        };


        sw_gps.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(sw_gps.isChecked()){
                    //most accurate - using GPS
                    locationRequest.setPriority(Priority.PRIORITY_HIGH_ACCURACY);
                    tv_sensor.setText("Using GPS sensors");
                }
                else{
                    locationRequest.setPriority(Priority.PRIORITY_BALANCED_POWER_ACCURACY);
                    tv_sensor.setText("Using towers + WIFI");
                }
            }
        });

        sw_locationupdates.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if(sw_locationupdates.isChecked()){
                    //turn on location tracking
                    startLocationUpdates();
                }
                else {
                    //turn off location tracking
                    stopLocationUpdates();
                }
            }
        });

        tv_navMessage.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence charSequence, int i, int i1, int i2) {

            }

            @Override
            public void onTextChanged(CharSequence charSequence, int i, int i1, int i2) {
                String s = tv_navMessage.getText().toString();
                int j = 0;
//                thread.send(s);
            }

            @Override
            public void afterTextChanged(Editable editable) {

            }
        });


//        thread.close();

        updateGPS();
    }// end onCreate method

    @Override
    protected void onStop() {
        super.onStop();
        //wakelock.release();
    }

    private void stopLocationUpdates() {
        tv_updates.setText("Location is NOT being tracked");
        tv_lat.setText("Not tracking location");
        tv_lon.setText("Not tracking location");
        tv_speed.setText("Not tracking location");
        tv_address.setText("Not tracking location");
        tv_accuracy.setText("Not tracking location");
        tv_altitude.setText("Not tracking location");
        tv_sensor.setText("Not tracking location");

        fusedLocationProviderClient.removeLocationUpdates(locationCallBack);
    }

    private void startLocationUpdates() {
        tv_updates.setText("Location is being tracked");
        fusedLocationProviderClient.requestLocationUpdates(locationRequest,locationCallBack,null);
        updateGPS();

    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);

        switch (requestCode){
            case PERMISSIONS_FINE_LOCATION:
                if(grantResults[0] == PackageManager.PERMISSION_GRANTED){
                    updateGPS();
                }
                else{
                    Toast.makeText(this, "This app requires permission to be granted in order to work properly", Toast.LENGTH_LONG).show();
                    finish();
                }
        }
    }

    private void updateGPS(){
        //get permission from the user to track GPS
        //get the current location from the fused client
        //update the UI - i.e. set all properties in their associated text view items

        fusedLocationProviderClient = LocationServices.getFusedLocationProviderClient(MainActivity.this);

        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_GRANTED){
            //user provided the permission
            fusedLocationProviderClient.getLastLocation().addOnSuccessListener(this, new OnSuccessListener<Location>() {
                @Override
                public void onSuccess(Location location) {
                    // we got permissions. Put the values of location. XXX into the UI components
                    updateUIValues(location);
                    currentLocation = location;
                    mGpsContainer.registerNavigation();
                }
            });
        }
        else{
            //permission not granted yet
            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M){
                requestPermissions(new String[] {Manifest.permission.ACCESS_FINE_LOCATION}, PERMISSIONS_FINE_LOCATION);
            }
        }
    }

    private void updateUIValues(Location location) {
        //update all the text view objects with the new location
        tv_lat.setText(String.valueOf(location.getLatitude()));
        tv_lon.setText(String.valueOf(location.getLongitude()));
        tv_accuracy.setText(String.valueOf(location.getAccuracy()));

        if(location.hasAltitude()){
            tv_altitude.setText(String.valueOf(location.getAltitude()));
        }
        else{
            tv_altitude.setText("Not available");
        }
        if(location.hasSpeed()){
            tv_speed.setText(String.valueOf(location.getSpeed()));
        }
        else{
            tv_speed.setText("Not available");
        }

        Geocoder geocoder = new Geocoder(MainActivity.this);
        try {
            List<Address> addresses = geocoder.getFromLocation(location.getLatitude(), location.getLongitude(), 1);
            tv_address.setText(addresses.get(0).getAddressLine(0));
        }
        catch (Exception e){
            tv_address.setText("Unable to get street address");
        }

        MyApplication myApplication = (MyApplication) getApplicationContext();
        savedLocations = myApplication.getMyLocations();

        //show the number of waypoints saved
        tv_wayPointCounts.setText(String.valueOf(savedLocations.size()));
    }

    private void startSocket(){
        try{
//            socket = new Socket("10.63.140.75", 10000);
            socket = new Socket("10.62.53.89", 10000);
        }catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void sendLine(String line){
        try{
            socket.getOutputStream().write(line.getBytes());
        }catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void sendLine2(String line){
        try {
            Socket socket = new Socket("10.63.140.75", 10000);
            socket.getOutputStream().write("line".getBytes());

            socket.close();
            runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    Toast.makeText(MainActivity.this, "Archivo enviado correctamente", Toast.LENGTH_SHORT).show();
                }
            });
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private void sendLine3(String s) {
        try {
//            Socket socket = new Socket("192.168.1.104", 10000);
            Socket socket = new Socket("10.63.140.75", 10000);

            socket.getOutputStream().write(s.getBytes());

            socket.close();
            runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    Toast.makeText(MainActivity.this, "Archivo enviado correctamente", Toast.LENGTH_SHORT).show();
                }
            });
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void closeSocket(){
        try{
            socket.close();
        }catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void sendFileContentsViaSocket() {
        try {
//            Socket socket = new Socket("192.168.1.104", 10000);
            Socket socket = new Socket("10.63.140.75", 10000);
            BufferedReader reader = new BufferedReader(new InputStreamReader(getAssets().open("train.json")));
            String line;

            while ((line = reader.readLine()) != null) {
                // Envía la línea al servidor a través del socket
                socket.getOutputStream().write(line.getBytes());

            }

//            for(int a = 0; a<10; a++){
//                socket.getOutputStream().write("Hello".getBytes());
////                socket.getOutputStream().flush();
//            }
//            socket.getOutputStream().write("END".getBytes());

            socket.close();
            reader.close();
            runOnUiThread(new Runnable() {
                @Override
                public void run() {
                    Toast.makeText(MainActivity.this, "Archivo enviado correctamente", Toast.LENGTH_SHORT).show();
                }
            });
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void forceTextViewChange(){
        while(true){
            if(this.threadStatus==true){
                break;
            }
        }
        for(int b = 0; b<10; b++){
            tv_navMessage.setText("Hello"+b);
        }
        tv_navMessage.setText("END");

        while(true){
            if(tv_navMessage.getText().toString()=="END"){
                break;
            }
        }
    }
    private void forceTextViewChange2(){
        for(int b = 0; b<10; b++){
            tv_navMessage.setText("Hello"+b);
        }
        tv_navMessage.setText("END");
//        thread.close();
    }

    private void endMessage(){
        tv_navMessage.setText("END");
//        thread.close();
    }
}