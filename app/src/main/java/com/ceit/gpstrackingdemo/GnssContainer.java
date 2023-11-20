/*
 * Copyright (C) 2017 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.ceit.gpstrackingdemo;

import android.content.Context;
import android.location.GnssMeasurementsEvent;
import android.location.GnssNavigationMessage;
import android.location.GnssStatus;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.location.OnNmeaMessageListener;
import android.os.Bundle;
import android.os.Environment;
import android.os.SystemClock;
import android.util.Log;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Arrays;
import java.util.Date;
import java.util.List;
import java.util.concurrent.TimeUnit;

public class GnssContainer {

  public static Context ctxt;
  public TextView navMessageOut;
  public static File logFile;
  public int messageCounter = 0;

  private boolean mLogNavigationMessages = true;

  private final List<GnssListener> mLoggers = null;

  private final LocationManager mLocationManager;
  private ServerCommunicationThread ServerCommThread;

  public GnssContainer(Context context, TextView tv) {
    ctxt = context;
    mLocationManager = (LocationManager) context.getSystemService(Context.LOCATION_SERVICE);
    navMessageOut = tv;

    SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
    String filename  = dateFormat.format(new Date());
    logFile = new File(ctxt.getFilesDir(),String.valueOf(filename)+".txt");
  }
  public GnssContainer(Context context) {
    ctxt = context;
    mLocationManager = (LocationManager) context.getSystemService(Context.LOCATION_SERVICE);
    ServerCommThread = new ServerCommunicationThread("localhost");
    ServerCommThread.start();

    SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
    String filename  = dateFormat.format(new Date());
    logFile = new File(ctxt.getFilesDir(),String.valueOf(filename)+".txt");
  }

  public void registerNavigation() {
    mLocationManager.registerGnssNavigationMessageCallback(gnssNavigationMessageListener);
  }

//  private final GnssNavigationMessage.Callback gnssNavigationMessageListener =
//      new GnssNavigationMessage.Callback() {
//
//        @Override
//        public void onGnssNavigationMessageReceived(GnssNavigationMessage event) {
//          if (mLogNavigationMessages) {
//            int describeContents = event.describeContents();
//            byte[] data = event.getData();
//            int messageId = event.getMessageId();
//            int status = event.getStatus();
//            int submessageId = event.getSubmessageId();
//            int svid = event.getSvid();
//            int type = event.getType();
//            SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
//
//            Date date = new Date();
//            long millisInString = date.getTime();
//
//            //--------------------------------------------------------------------------
//            // - ultiliza el fichero txt creado en el constructor de GnssContainer
//            int i = 0;
//            if(i==0){
////            if (type == 1537){
//              FileWriter fileWriter = null;
//              try {
//                fileWriter = new FileWriter(logFile,true);
//                BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
//                if (messageCounter == 0){
//                  bufferedWriter.write("# Svid,Timestamp,Type,Status,MessageId,Sub-messageId,Data(Bytes)\n");
//                }
//                String newLine = String.format("%s,%s,%s,%s,%s,%s,%s",svid,millisInString,type,status,messageId,submessageId,Arrays.toString(data));
//                Log.d("NavMsg",newLine);
//                bufferedWriter.write(newLine);
//                bufferedWriter.write("\n");
//                bufferedWriter.close();
//                fileWriter.close();
//                navMessageOut.setText(newLine);
//              } catch (IOException e) {
//                throw new RuntimeException(e);
//              }
//
//              messageCounter += 1;
//              if (messageCounter >= 50){
//                messageCounter=50;
//              }
//            }
//
//            // - fin
//            //--------------------------------------------------------------------------
//          }
//        }
//
//        @Override
//        public void onStatusChanged(int status) {
//          if (mLogNavigationMessages) {
//            for (GnssListener logger : mLoggers) {
//              logger.onGnssNavigationMessageStatusChanged(status);
//            }
//          }
//        }
//      };
  private final GnssNavigationMessage.Callback gnssNavigationMessageListener =
          new GnssNavigationMessage.Callback() {

            @Override
            public void onGnssNavigationMessageReceived(GnssNavigationMessage event) {
              if (mLogNavigationMessages) {
                int describeContents = event.describeContents();
                byte[] data = event.getData();
                int messageId = event.getMessageId();
                int status = event.getStatus();
                int submessageId = event.getSubmessageId();
                int svid = event.getSvid();
                int type = event.getType();
                SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");

                Date date = new Date();
                long millisInString = date.getTime();

                //--------------------------------------------------------------------------
                // - ultiliza el fichero txt creado en el constructor de GnssContainer
                int i = 0;
                if(i==0){
//            if (type == 1537){
                  FileWriter fileWriter = null;
                  try {
                    fileWriter = new FileWriter(logFile,true);
                    BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
                    if (messageCounter == 0){
                      bufferedWriter.write("# Svid,Timestamp,Type,Status,MessageId,Sub-messageId,Data(Bytes)\n");
                    }
                    String newLine = String.format("%s,%s,%s,%s,%s,%s,%s",svid,millisInString,type,status,messageId,submessageId,Arrays.toString(data));
                    Log.d("NavMsg",newLine);
                    bufferedWriter.write(newLine);
                    bufferedWriter.write("\n");
                    bufferedWriter.close();
                    fileWriter.close();
                    ServerCommThread.send(newLine);
                  } catch (IOException e) {
                    throw new RuntimeException(e);
                  }

                  messageCounter += 1;
                  if (messageCounter >= 50){
                    messageCounter=50;
                  }
                }

                // - fin
                //--------------------------------------------------------------------------
              }
            }

            @Override
            public void onStatusChanged(int status) {
              if (mLogNavigationMessages) {
                for (GnssListener logger : mLoggers) {
                  logger.onGnssNavigationMessageStatusChanged(status);
                }
              }
            }
          };





}
