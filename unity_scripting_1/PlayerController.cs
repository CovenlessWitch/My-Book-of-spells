using UnityEngine;
using UnityEngine.InputSystem;
[RequireComponent(typeof(Rigidbody2D))]
public class PlayerController : MonoBehaviour
{
    public float walkSpeed = 5f;
    Vector2 moveInput;
    [SerializeField]
    private bool _isMoving = false;

    public bool IsMoving 
    { get => _isMoving;
      private set
      {
        _isMoving = value;
        animator.SetBool("isMoving", value);
      }
    }  

    public bool _isFacingRight = true; 

    public bool IsFacingRight 
    {get {return _isFacingRight;} private set{
     if(_isFacingRight != value)
     {
        transform.localScale *= new Vector2(-1, 1);
     }
    _isFacingRight = value; 

    }} 
    Rigidbody2D rb;
    Animator animator;

    private void Awake() 
    {
        rb = GetComponent<Rigidbody2D>();
        animator = GetComponent<Animator>();
    }


    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void FixedUpdate() 
    {
        rb.linearVelocity = new Vector2(moveInput.x * walkSpeed,rb.linearVelocity.y);
    }
    public void OnMove(InputAction.CallbackContext context) 
    {
        moveInput = context.ReadValue<Vector2>();

        IsMoving = moveInput != Vector2.zero;

        SetFacingDirection(moveInput);

    }
  private void SetFacingDirection(Vector2 moveInput)
  {
    if(moveInput.x > 0 && !IsFacingRight)
    {
       
       // Face the right
       IsFacingRight = true;

    }
    else if (moveInput.x < 0 && IsFacingRight)
    {
        // Face left

        IsFacingRight = false;
    }
    
  }
} 
