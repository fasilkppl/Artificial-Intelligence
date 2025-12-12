const BackgroundImage = () => {
  return (
    <>
      {/* Background Image with Blur */}
      <div 
        className="fixed inset-0 z-0"
        style={{
          backgroundImage: `url('https://images.unsplash.com/photo-1564013799919-ab600027ffc6?ixlib=rb-4.0.3&auto=format&fit=crop&w=2070&q=80')`,
          backgroundSize: 'cover',
          backgroundPosition: 'center',
          backgroundRepeat: 'no-repeat',
          filter: 'blur(8px)',
          transform: 'scale(1.1)',
        }}
      />
      
      {/* Dark Overlay */}
      <div 
        className="fixed inset-0 z-0"
        style={{
          background: 'linear-gradient(135deg, rgba(15, 23, 42, 0.7) 0%, rgba(30, 41, 59, 0.8) 100%)',
        }}
      />
      
      {/* Gradient Glow */}
      <div 
        className="fixed inset-0 z-0 opacity-30"
        style={{
          background: 'radial-gradient(ellipse at 50% 0%, hsl(174 72% 56% / 0.3) 0%, transparent 50%)',
        }}
      />
    </>
  );
};

export default BackgroundImage;
