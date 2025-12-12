import PricePredictor from "@/components/PricePredictor";
import BackgroundImage from "@/components/BackgroundImage";

const Index = () => {
  return (
    <div className="relative min-h-screen flex items-center justify-center p-4 overflow-hidden">
      <BackgroundImage />
      
      {/* Content */}
      <div className="relative z-10 w-full flex flex-col items-center">
        {/* Floating decorative elements */}
        <div 
          className="absolute -top-20 -left-20 w-64 h-64 rounded-full opacity-20 animate-float"
          style={{
            background: 'radial-gradient(circle, hsl(174 72% 56% / 0.5) 0%, transparent 70%)',
            animationDelay: '0s',
          }}
        />
        <div 
          className="absolute -bottom-20 -right-20 w-80 h-80 rounded-full opacity-15 animate-float"
          style={{
            background: 'radial-gradient(circle, hsl(142 52% 65% / 0.5) 0%, transparent 70%)',
            animationDelay: '3s',
          }}
        />
        
        {/* Main Content */}
        <PricePredictor />
        
        {/* Footer */}
        <p className="mt-6 text-xs text-muted-foreground/60 animate-fade-in" style={{ animationDelay: "0.6s" }}>
          Powered by Machine Learning
        </p>
      </div>
    </div>
  );
};

export default Index;
