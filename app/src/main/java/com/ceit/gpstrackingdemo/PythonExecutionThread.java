package com.ceit.gpstrackingdemo;

import android.content.Context;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

public class PythonExecutionThread extends Thread{
    private Context mContext;
    public PythonExecutionThread(Context context) {
        this.mContext = context;
    }
    @Override
    public void run(){
        Python.start( new AndroidPlatform(mContext));
        Python python = Python.getInstance();
        PyObject pyObject = python.getModule("main").callAttr("main");
    }
}
