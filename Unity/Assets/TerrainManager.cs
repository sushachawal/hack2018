using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class TerrainManager : MonoBehaviour {

    public CSVParsing cvs1;
    public static TerrainManager instance;
    public LineRenderer lineRenderer;

    private Vector3[] heightMap;
    private float[] velocities;
    public float multiplier_y = 2;
    
    float angle = 180f;
    void Awake()
    {
        instance = this;
    }
	void Start () {
        int points = cvs1.xData.Length;
        Debug.Log(points);
        heightMap = new Vector3[points];
        velocities = new float[points - 1];
        for(int i = 0; i < points; i++)
        {
            Vector3 vec = new Vector3(cvs1.xData[i], multiplier_y * cvs1.yData[i], 0);
            //heightMap[i].x = CSVParsing.instance.xData[i];
            //heightMap[i].y = CSVParsing.instance.yData[i];
            //heightMap[i].z = 0;
            heightMap[i] = vec;
            if (i < points - 1) velocities[i] = cvs1.velocity[i];
        }
        lineRenderer.positionCount = heightMap.Length;
        lineRenderer.SetPositions(heightMap);
        //instance = this;
		//for(int i = 0; i < heightMap.Length; i++)
        //{
            
           // heightMap[i].x = 1.0f * i / heightMap.Length;
            //heightMap[i].y = 0.1f * Mathf.Sin(angle * (Mathf.PI / 180) *i/ (heightMap.Length - 1));
           // heightMap[i].z = 0;
            //if (i != 0) Gizmos.DrawLine(heightMap[i - 1], heightMap[i]);
       // }
	}

    // Update is called once per frame
    void Update () {
		
	}
    public float getInclination(float x)
    {
        float inc = 0;
        for (int i = 1; i < heightMap.Length; i++)
        {
            if (x < heightMap[i].x)
            {
                inc = Mathf.Atan2((heightMap[i].y - heightMap[i - 1].y), (heightMap[i].x - heightMap[i-1].x));
                break;
            }
        }
        return inc;
    }
    public float getCurvature(float x)
    {
        float prevSlope = 0;
        float nextSlope = 0;
        float curv = 0;
        for (int i = 1; i < (heightMap.Length - 1); i++)
        {
            float deltaX = (heightMap[i].x - heightMap[i - 1].x);
            prevSlope = (heightMap[i].y - heightMap[i - 1].y) / deltaX;
            
            nextSlope = (heightMap[i + 1].y - heightMap[i].y) / deltaX;
            if (Mathf.Abs(x - heightMap[i].x) < deltaX / 2)
            {
               // Debug.Log("dx: " + deltaX);
               // Debug.Log("PrevSlope: " + prevSlope);
               // Debug.Log("Slope: " + nextSlope);
                curv = (nextSlope - prevSlope)/deltaX;
                break;
            }
        }
        return curv;
    }
}
