using UnityEngine;
using UnityEngine.UI;


public class HealtBar : MonoBehaviour
{
    public Slider healthSlider;

    public void SetHeath(int health)
    {
        healthSlider.value = health;
    }
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
