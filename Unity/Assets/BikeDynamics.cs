using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class BikeDynamics : MonoBehaviour {
    public CSVParsing parsing;
    Rigidbody rgb;
    private int piece= 0;
    private const float v_const = 30f;
    private Vector3 velocityO;
    void Start()
    {
        rgb = GetComponent<Rigidbody>();
        UpdateBobA();
        UpdateBob();
        
    }
    void FixedUpdate()
    {
        transform.position += velocityO * Time.deltaTime;
        Debug.Log(velocityO);
    }
	void Update () {
        if(transform.position.x > parsing.xData[piece])
        {
            UpdateBobA();
            piece++;
            if (piece >= parsing.xData.Length) Application.LoadLevel(Application.loadedLevel);
            UpdateBob();
        }
    }
    void UpdateBobA()
    {
        transform.position = new Vector3(parsing.xData[piece], TerrainManager.instance.multiplier_y * parsing.yData[piece], 0);
    }
    void UpdateBob()
    {
        
        velocityO = v_const * parsing.velocity[piece] * getVelocityDirection(piece);
       // Debug.Log(getVelocityDirection(piece).magnitude);
    }
    private Vector3 getVelocityDirection(int i)
    {
        float angle = Mathf.Atan(TerrainManager.instance.multiplier_y * (parsing.yData[i + 1] - parsing.yData[i]) / (parsing.xData[i + 1] - parsing.xData[i]));
        return new Vector3(Mathf.Cos(angle), Mathf.Sin(angle), 0);
    }
}
